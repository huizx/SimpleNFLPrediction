# NFL Game predictor
# Authors:  Ben Spencer and Tony Hui
# get the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.svm import SVC

# read in the data
nfl = pd.read_csv('nfl_games.csv')
# print(nfl.describe())

# Team names
TEAMS = ['Cowboys', 'Buccaneers', 'Eagles', 'Falcons', 'Steelers',
         'Bills', 'Jets', 'Panthers', 'Vikings',
         'Bengals', '49ers', 'Lions', 'Jaguars',
         'Seahawks', 'Colts', 'Cardinals', 'Titans',
         'Chargers', 'Commanders', 'Browns', 'Chiefs',
         'Dolphins', 'Patriots', 'Packers', 'Saints',
         'Broncos', 'Bears', 'Rams', 'Raiders', 'Ravens']

# print(nfl.info())

# load the data
feature_cols = nfl[['PointsScored', 'PointsGivenUp', 'First Downs', 'NetYards', 'DYards', 'NetRushing',
                    'DRushing', 'NetPassing', 'DPassing', 'Punts', 'Possession', 'NumOfPlays', '3rd Down %']]
feature_cols = feature_cols.astype(np.bool)
X = nfl[feature_cols]
y = nfl.Outcome
# print(feature_cols.info())
# split the training data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y)
X_train = X_train.astype(np.bool)
# print(X_train.info())
# normalize or standardize features
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_test_std = X_test_std.astype(np.bool)

# build the model
model = SVC(kernel='rbf', C=1)
model.fit(X_train, y_train)

# enter the teams you want to predict
home_team = input('Enter the home team: ')

# get data for the home team
home_data = nfl[nfl['Team'] == home_team]
n_home_data = home_data.drop(['Team', 'Outcome'], axis=1)
# predict the outcome
X_new = home_data
X_new = X_new.astype(np.bool)
X_new_std = sc.transform(X_new)
y_hat = model.predict(X_new)
print(y_hat)

y_hats = model.predict(X_test_std)
print(y_hats)
model.decision_function(X_test_std)
print(y_test)
