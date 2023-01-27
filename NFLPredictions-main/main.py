# NFL Game predictor
# Authors:  Ben Spencer and Tony Hui
# get the libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split


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

# enter the teams you want to predict
home_team = input('Enter the home team: ')
away_team = input('Enter the away team: ')

# get the data for the teams you want to predict
home_data = nfl[(nfl['Team'] == home_team)]
away_data = nfl[(nfl['Team'] == away_team)]

# get the features and the labels
home_features = home_data[['PointsScored', 'PointsGivenUp', 'First Downs', 'NetYards', 'DYards', 'NetRushing',
                           'DRushing', 'NetPassing', 'DPassing', 'Punts', 'Possession', 'NumOfPlays', '3rd Down %',
                           'Outcome']]
away_features = away_data[['PointsScored', 'PointsGivenUp', 'First Downs', 'NetYards', 'DYards', 'NetRushing',
                           'DRushing', 'NetPassing', 'DPassing', 'Punts', 'Possession', 'NumOfPlays', '3rd Down %',
                           'Outcome']]

# drop Outcome column
n_home_data = home_features.drop(['Outcome'], axis=1)
n_away_data = away_features.drop(['Outcome'], axis=1)

# get average scores for the teams you want to predict
home_avg = n_home_data.mean()
away_avg = n_away_data.mean()

# assign X and y
X_home = home_avg
y = home_features['Outcome']

# reshape the data
X_home = X_home.values.reshape(-1, 1)
y = y.values.reshape(-1, 1)

print(X_home.shape)
print(y.shape)

# split the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X_home, y, test_size=0.2, random_state=42)

# create the model
model = LinearRegression()

# fit the model
model.fit(X_train, y_train)

# predict the scores
predicted_home = model.predict(X_test)

