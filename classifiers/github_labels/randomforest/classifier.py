import sys
import pickle
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.model_selection import GridSearchCV

sys.path.append("../../../libs")
from dataset import loadData
from datapreprocessing import preprocess

dataset_name = "github-issue-bug-enhancement"
ratio = 90
 
print ("loading dataset %s from files" % dataset_name)
dataset = loadData(dataset_name, False)
labels = loadData(dataset_name, True)
reduceDatasetBy = 1

print ("dataset and labels loaded, splitting using cross_validation")
features_train, features_test, labels_train, labels_test = preprocess(dataset, labels, 1 - (ratio / 100))
 
 
features_train = features_train[:int(len(features_train) / reduceDatasetBy)]
labels_train = labels_train[:int(len(labels_train) / reduceDatasetBy)]

print ("Size of training data = %s" % len(labels_train))
print ("Size of test data = %s" % len(labels_test))

print ("performing automated feature seleciton")
print ("No of features before selection = %d" % len(features_train[0]))

selector = SelectPercentile(f_classif, percentile=95)
selector.fit(features_train, labels_train)
features_train = selector.transform(features_train)
features_test = selector.transform(features_test)
print ("No of features after selection = %d" % len(features_train[0]))

print ("training classifier using random forest ensemble")
_start = time.time()


# Applying grid GridSearchCV
# clf_rfc = RandomForestClassifier(min_samples_split=10)
# params = {'n_estimators': [50], 'criterion': ['gini', 'entropy']}
# clf = GridSearchCV(clf_rfc, params)

clf = RandomForestClassifier(n_estimators=50, min_samples_split=10, criterion='entropy')
clf.fit(features_train, labels_train)
_training_time = time.time() - _start
_start = time.time()

# if the GridSearchCV was performed
# print ("best params")
# print(clf.best_params_)
 
print ("predicting test data")
result = clf.predict(features_test)
_prediciton_time = time.time() - _start

precision, recall, fbetascore, support  = precision_recall_fscore_support(labels_test, result)
 
print ("training size - %s%%, test size - %s%% on dataset `%s`" % (ratio, 100 - ratio, dataset_name))
print ("Accuracy - %s, Classification Time - %s, Prediciton Time - %s" % (accuracy_score(result, labels_test), _training_time, _prediciton_time))
print ("Precision: %s, Recall: %s, F1_Score: %s" % (precision, recall, fbetascore))

print ("____ report ______")
print (classification_report(labels_test, result))