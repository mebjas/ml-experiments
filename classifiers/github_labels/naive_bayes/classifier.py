import pickle
from sklearn import naive_bayes
from sklearn.metrics import accuracy_score
from sklearn import cross_validation

def loadData(name, isLabel):
    data = []
    handle = None
    if isLabel:
        handle = open('../../../dataset/' +name +'/labels.pickle', 'rb');
    else:
        handle = open('../../../dataset/' +name +'/dataset.pickle', 'rb');
    data = pickle.load(handle)
    handle.close()
    return data;

dataset_name = "github-issue-bug-enhancement"

print ("loading dataset %s from files" % dataset_name)
dataset = loadData(dataset_name, False)
labels = loadData(dataset_name, True)

print ("dataset and labels loaded, splitting using cross_validation")
feature_train, feature_test, labels_train, labels_test = cross_validation.train_test_split(dataset, labels, test_size = 0.1, random_state=42)

print ("training classifier using naive bayes GaussianNB")
clf = naive_bayes.GaussianNB()
clf.fit(feature_train.toarray(), labels_train)

print ("predicting test data")
result = clf.predict(feature_test.toarray())

print ("accuracy score = ")
print (accuracy_score(result, labels_test))


