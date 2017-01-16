from sklearn import cross_validation
from sklearn.feature_selection import SelectPercentile, f_classif

def preprocess(dataset, labels, ratio):
    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(dataset, labels, test_size = ratio, random_state=42)

    ### feature selection, because text is super high dimensional and 
    ### can be really computationally chewy as a result

    selector = SelectPercentile(f_classif, percentile=10)
    selector.fit(features_train, labels_train)
    features_train = selector.transform(features_train).toarray()
    features_test  = selector.transform(features_test).toarray()

    return features_train, features_test, labels_train, labels_test