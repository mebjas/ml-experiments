import json, sys, pickle, time
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from nltk.stem.snowball import SnowballStemmer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV

## all parameters
test_size = 0.1
feature_selection_percentile = 12
reduceDatasetBy = 1
## all parameters


stemmer = SnowballStemmer("english")
issues = []
labels = []

print ("reading the dataset file + stemming")
with open('dataset_complete.json', encoding='utf8') as rd:
    data = json.load(rd)
    for d in data:
        if (d['label'].lower() == 'bug'): labels.append(0)
        else: labels.append(1)

        issue = " ".join([stemmer.stem(word) for word in d['issue'].split(" ")])
        issues.append(issue)

print ("No of data = %s" % len(issues))
print ("Test / Train ratio = %s, performing cross_validation" % test_size)
features_train, features_test, labels_train, labels_test= cross_validation.train_test_split(issues, labels, test_size=test_size, random_state=42)

print ("Vectorizing using tf idf transformer")

### text vectorization--go from strings to lists of numbers
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test)

### feature selection, because text is super high dimensional and 
### can be really computationally chewy as a result
print ("Features selection at %s percentile data" % feature_selection_percentile)
selector = SelectPercentile(f_classif, percentile=feature_selection_percentile)
selector.fit(features_train, labels_train)
features_train = selector.transform(features_train).toarray()
features_test  = selector.transform(features_test).toarray()
print ("Features after selection: %s" % len(features_train[0]))

print ("reducing data size by %s " % reduceDatasetBy)
features_train = features_train[:int(len(features_train) / reduceDatasetBy)]
labels_train = labels_train[:int(len(labels_train) / reduceDatasetBy)]
print ("size of training dataset = %s" % len(features_train))

# print ("Performing principal component analysis")
# pca = PCA()
# pca.fit(features_train)
# features_train = pca.transform(features_train)
# features_test = pca.transform(features_test)

print ("training classifier using randomforestensemble")
_start = time.time()

# # Applying grid GridSearchCV
# clf_rfc = RandomForestClassifier(n_estimators=20, criterion='gini')
# params = {'min_samples_split': [9, 10, 11]}
# clf = GridSearchCV(clf_rfc, params)

clf = RandomForestClassifier(n_estimators=20, min_samples_split=11, criterion='gini')
clf.fit(features_train, labels_train)
_training_time = time.time() - _start
_start = time.time()

# # if the GridSearchCV was performed
# print ("best params")
# print(clf.best_params_)

print ("predicting test data")
result = clf.predict(features_test)
_prediciton_time = time.time() - _start

precision, recall, fbetascore, support  = precision_recall_fscore_support(labels_test, result)
 
print ("training size - %s, test size - %s on dataset" % (1 - test_size, test_size))
print ("Accuracy - %s, Classification Time - %s, Prediciton Time - %s" % (accuracy_score(result, labels_test), _training_time, _prediciton_time))
print ("Precision: %s, Recall: %s, F1_Score: %s" % (precision, recall, fbetascore))

print ("____ report ______")
print (classification_report(labels_test, result))