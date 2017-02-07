# Random Forest Ensemble

### Initally started with `n_estimators=15` and `criterion=entropy` as they proved to be best for decisionTree and since random forest is based on that.

| training   size | features_percentile | n_estimators | criterion | training time | testing time | accuracy | training data   size | test data size |   |
|-----------------|---------------------|--------------|-----------|---------------|--------------|----------|----------------------|----------------|---|
| 90 by 10        |                     | 15           | entropy   | 22            | 0.5          | 78.27    |                      |                |   |
| 90 by 5         |                     | 15           | entropy   | 56            | 36.6         | 79.74    |                      |                |   |
| 90 by 1         |                     | 15           | entropy   | 1077          | 0.863        | 85.74    | 102052               | 11340          |   |
| 90 by 100       |                     | 15           | entropy   | 0.42155       | 0.37         | 74.25    | 1020                 | 11340          |   |
| 90 by 100       |                     | 15           | entropy   | 23            | 0.53         | 78.46    | 10205                | 11340          |   |
|                 |                     |              |           |               |              |          |                      |                |   |

### So as you can notice, max accuracy of `85.74%` was achieved for full dataset with `102052 training data` and `11340 test data`. However this took `1077 seconds` to train.

### dimentionality reduction using `feature_selection` was employed to get following result

| training   size | features_percentile | n_estimators | criterion | training time | testing time | accuracy | training data   size | test data size |   |
|-----------------|---------------------|--------------|-----------|---------------|--------------|----------|----------------------|----------------|---|
| 90 by 100       | 1                   | 15           | entropy   | 0.269         | 0.054454     | 74.4     | 10205                | 11340          |   |
| 90 by 100       | 10                  | 15           | entropy   | 1.2           | 0.161        | 76.95    | 10205                | 11340          |   |
| 90 by 100       | 20                  | 15           | entropy   | 1.99          | 0.2          | 77.6     | 10205                | 11340          |   |
| 90 by 100       | 50                  | 15           | entropy   | 3.56          | 0.3          | 78.253   | 10205                | 11340          |   |
| 90 by 100       | 75                  | 15           | entropy   | 4.4           | 0.36         | 78.43    | 10205                | 11340          |   |
| 90 by 100       | 85                  | 15           | entropy   | 4.3           | 0.38         | 78.13    | 10205                | 11340          |   |
| 90 by 100       | 80                  | 15           | entropy   | 4.28          | 0.36         | 78.28    | 10205                | 11340          |   |
| 90 by 1         | 1                   | 15           | entropy   | 4.5           | 0.08         | 79.7     | 102052               | 11340          |   |
| 90 by 1         | 10                  | 15           | entropy   | 33.4          | 0.27         | 83.76    | 102052               | 11340          |   |
| 90 by 1         | 20                  | 15           | entropy   | 56            | 0.4          | 84.01    | 102052               | 11340          |   |
| 90 by 1         | 50                  | 15           | entropy   | 97            | 0.58         | 85.32    | 102052               | 11340          |   |
| 90 by 1         | 75                  | 15           | entropy   | 123           | 0.76         | 85.41    | 102052               | 11340          |   |
| 90 by 1         | 80                  | 15           | entropy   | 125.4         | 0.815        | 85.55    | 102052               | 11340          |   |
| 90 by 1         | 85                  | 15           | entropy   | 126.54        | 0.844        | 85.52    | 102052               | 11340          |   |
| *90 by 1*         | 90                  | 15           | entropy   | *127.8*         | *0.84*         | *85.71*    | 102052               | 11340          |   |
| 90 by 1         | 95                  | 15           | entropy   | 129           | 0.87         | 85.8     | 102052               | 11340          |   |
| 90 by 1         | 100                 | 15           | entropy   | 130           | 0.86         | 0.8522   | 102052               | 11340          |   |


### Summary so far: with feature seleciton (percentile = 90) an accuracy of `85.71%` was achieved with same amout of dataset as in last experiment (`102052 training data` and `11340 test data`).
### However training time reduced to `127s = around 2 minutes`.
### look at report.xlsx for better overview.