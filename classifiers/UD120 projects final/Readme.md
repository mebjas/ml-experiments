# Report based on Udacity UD120 

| Accuracy      | Precision | Recall | F1     | F2      | Action                                                                          |
|---------------|-----------|--------|--------|---------|---------------------------------------------------------------------------------|
| 0.777         | 0.24      | 0.31   | 0.27   | 0.30032 |                                                                                 |
|               |           |        |        |         | NB -> randomforest + PCA + GridSearchCV                                         |
| 0.83383       | 0.32      | 0.19   | 0.23   | 0.2     |                                                                                 |
|               |           |        |        |         | removed salary as a feature                                                     |
| 0.84          | 0.335     | 0.2    | 0.25   | 0.21    |                                                                                 |
|               |           |        |        |         | feature - 95 %ile                                                               |
| 0.8384        | 0.332     | 0.209  | 0.25   | 0.22    |                                                                                 |
|               |           |        |        |         | feature 100%ile                                                                 |
| 0.83967       | 0.33026   | 0.197  | 0.24   | 0.21    |                                                                                 |
|               |           |        |        |         | feature 80%ile                                                                  |
| 0.837         | 0.316     | 0.191  | 23     | 0.2     |                                                                                 |
|               |           |        |        |         | selectKBest = 10                                                                |
| 0.837         | 0.32      | 0.202  | 0.24   | 0.21    |                                                                                 |
|               |           |        |        |         | selectKBest = 15                                                                |
| 0.8437        | 0.357     | 0.215  | 0.268  | 0.23    |                                                                                 |
|               |           |        |        |         | selectKBest = 16                                                                |
| 0.838         | 0.326     | 0.199  | 0.24   | 0.21    |                                                                                 |
|               |           |        |        |         | selectKBest = 14                                                                |
| 0.839         | 0.33      | 0.211  | 0.26   | 0.22    |                                                                                 |
|               |           |        |        |         | selectKBest = 15, rfc criterion = entropy, n_estimator = 2, min_sample_split =2 |
| 0.854         | 0.3367    | 0.097  | 0.151  | 0.113   |                                                                                 |
|               |           |        |        |         | criterion = gini                                                                |
| 0.849         | 0.3       | 0.1    | 0.15   | 0.11    |                                                                                 |
|               |           |        |        |         | removed pca                                                                     |
| 0.8546        | 0.409     | 0.203  | 0.27   | 0.22    |                                                                                 |
|               |           |        |        |         | random forest -> SVM.svc, linear                                                |
| too much time |           |        |        |         | random forest -> feature scaling minmaxscaler                                   |
|               |           |        |        |         | adaboost <5, SAMME.R>                                                           |
| 0.8565        | 0.433     | 0.24   | 0.316  | 0.27    |                                                                                 |
|               |           |        |        |         | adaboost <10, SAMME.R>                                                          |
| 0.86          | 0.4637    | 0.317  | 0.3766 | 0.33842 |                                                                                 |
|               |           |        |        |         | adaboost <10, SAMME> after gridsearchcv                                         |
| 0.866         | 0.501     | 0.313  | 0.385  | 0.33845 |                                                                                 |
|               |           |        |        |         | using PCA degraded metrics                                                      |
|               |           |        |        |         | using selectKBest=16 same result                                                |
|               |           |        |        |         | using selectKBest=17 same result                                                |
|               |           |        |        |         | all features -> 22, using 18 best                                               |
|               |           |        |        |         | revert back to  adaboost <10, SAMME>                                            |
| 0.86693       | 0.501     | 0.3135 | 0.3858 | 0.33892 |                                                                                 |

