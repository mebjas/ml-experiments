import sys
import pickle
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectPercentile, f_classif

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

selector = SelectPercentile(f_classif, percentile=50)
selector.fit(features_train, labels_train)
features_train = selector.transform(features_train) #.toarray()
features_test = selector.transform(features_test) #.toarray()
print ("No of features after selection = %d" % len(features_train[0]))


print ("training classifier using random forest ensemble")
_start = time.time()
clf = RandomForestClassifier(n_estimators=15, criterion="entropy")
clf.fit(features_train, labels_train)
_training_time = time.time() - _start
_start = time.time()
 
print ("predicting test data")
result = clf.predict(features_test)
_prediciton_time = time.time() - _start
 
print ("training size - %s%%, test size - %s%% on dataset `%s`" % (ratio, 100 - ratio, dataset_name))
print ("Accuracy - %s, Classification Time - %s, Prediciton Time - %s" % (accuracy_score(result, labels_test), _training_time, _prediciton_time))
 