# Machine Learning Experiments Server
This is my kind of first hands on experimentation with machine learning algorithms and techniques. I'll keep updating my summaries here:

### Experiment 1: Classifier to classify a Github Issue as `enhancement` or `bug` based purely on issue title.
#### Quick Summary: Mined more that `1,00,000` Issue data from Github open source repositories. Most of them were `enhancement` or `bugs`. Tried a couple of alogirthms and techniques on them. And here's things I have learnt so far.
 - Training result (accuracy) seemed to go up with training data size (no of rows).
 - But for few ML algorithms, training time also go up with training data. Few algorithms seemed to take time proportional to training data while predicting. For example - `Gaussian Naive Bayes`, `SVM`. While it was pretty much constant in case of tree based algorithms like - `decision tree`, `random forest`, `adaboost with decision tree as weak learner`.
 - Here's the best accuracy I could achive so far with diff algorithms (w/o mentioning the parameters or training time or data size).
 
  Algorithm     | Accuracy (%)  |
  ------------- |---------------|
  SVM           | 80.08         |
  AdaBoost      | 74.82         |
  Naive Bayes   | 68.84         |
  ***Random Forest*** | ***85.8***         |
  Decision Tree | 77.52         |
  
  Which made me an obvious fan of `Random Forest Ensemble` considering both speed and accuracy.
  
 - In my case ***feature selection only seemed to improve the accuracy of `random forest classifier` by small margin***. Best results were observed `95 percentile` feature selection was applied. Without any feature selection in pipeline it was `85.74% accuracy` for same amount of data and parameters (`n_estimators = 15`, `criterio=entropy`). **However the training time reduced to `129s` with `95%ile` feature selection contrary to when it was not applied** when it took `1077s` -> Nearly 8 times. One thing of interest was the results - accuracy (marginal diff though) and training time were different when feature selection with 100%ile selection and no feature selection was applied. In case of 100%ile selection time it took was `130s` in place of `1077s`.
 
 - ***Accuracy is not the only metric to consider - metrics like precision, recall & f1_score are important too***. At it's best got following data. Note that there were two labels so metrics like precisio, recall & fbeta will have two values
 
  - | - | - |
  ------------  | ---------- | ----------- |
 Random Forest | accuracy = `85.34%` | precision = `[0.87, 0.82]` |
 recall = `[0.92, 0.73]`| fbeta_score = `[0.89, 0.77]`||
 
#### TODOS / Things to test
 - [ ] Feature Cleaning pipeline
    - [ ] Stemming of issue text
    - [ ] Removing stopwords
 - [ ] Principal Component Analysis
 - [ ] GridSearchCV to find best parameters for classifier.
