import sys
import pickle
import time
from sklearn import tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

sys.path.append("../../../libs")
from dataset import loadData
from datapreprocessing import preprocess

# variables
dataset_name = "github-issue-bug-enhancement"
ratio = 90
min_samples_split = 500
criterion="entropy"

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
 
print ("loading dataset %s from files" % dataset_name)
dataset = loadData(dataset_name, False)
labels = loadData(dataset_name, True)
reduceDatasetBy = 100


print ("dataset and labels loaded, splitting using cross_validation")
features_train, features_test, labels_train, labels_test = preprocess(dataset, labels, 1 - (ratio / 100))
 
 
features_train = features_train[:int(len(features_train) / reduceDatasetBy)]
labels_train = labels_train[:int(len(labels_train) / reduceDatasetBy)]
 
print ("Size of training data = %s" % len(labels_train))
print ("Size of test data = %s" % len(labels_test))

print ("training classifier using decision tree")
_start = time.time()
clf = tree.DecisionTreeClassifier(min_samples_split=min_samples_split, criterion=criterion)
clf.fit(features_train, labels_train)
_training_time = time.time() - _start
_start = time.time()
 
print ("predicting test data")
result = clf.predict(features_test)
_prediciton_time = time.time() - _start
 
print ("training size - %s%%, test size - %s%% on dataset `%s`" % (ratio, 100 - ratio, dataset_name))
print ("Accuracy - %s, Classification Time - %s, Prediciton Time - %s" % (accuracy_score(result, labels_test), _training_time, _prediciton_time))