import pandas as pd

from format_submission import format_submission

#### 1. Importing and Preparing Data ####


print("Step 1/4: Importing and Preparing Data")

train_station = pd.read_csv("train.csv", sep=",")
train_station['date'] = pd.to_datetime(train_station['date'])
train_station['Postcode'] = train_station['Postcode'].astype(str)

test_station = pd.read_csv("test.csv", sep=",")
test_station['date'] = pd.to_datetime(test_station['date'])
test_station['Postcode'] = test_station['Postcode'].astype(str)

train_area = train_station.groupby(['date', 'area']).agg({'Available': 'sum',
                                                         'Charging': 'sum',
                                                          'Passive': 'sum',
                                                          'Other': 'sum',
                                                          'tod': 'max',
                                                          'dow': 'max',
                                                          'Latitude': 'mean',
                                                          'Longitude': 'mean',
                                                          'trend': 'max'}).reset_index()
test_area = test_station.groupby(['date', 'area']).agg({
    'tod': 'max',
    'dow': 'max',
    'Latitude': 'mean',
    'Longitude': 'mean',
    'trend': 'max'}).reset_index()


train_global = train_station.groupby('date').agg({'Available': 'sum',
                                                  'Charging': 'sum',
                                                  'Passive': 'sum',
                                                  'Other': 'sum',
                                                  'tod': 'max',
                                                  'dow': 'max',
                                                  'trend': 'max'}).reset_index()
test_global = test_station.groupby('date').agg({
    'tod': 'max',
    'dow': 'max',
    'trend': 'max'}).reset_index()

#### 2. Target Analysis ####

print("Step 2/4: Target Analysis")

station_features = ['Station', 'tod', 'dow', 'area'] + \
    ['trend', 'Latitude', 'Longitude']  # temporal and spatial inputs
area_features = ['area', 'tod', 'dow'] + ['trend',
                                          'Latitude', 'Longitude']  # temporal and spatial inputs
global_features = ['tod', 'dow'] + ['trend']  # temporal input

#### 3. Modelling ####

print("Step 3/4: Modelling")

s_naive = train_station.drop(["date", "trend", "Latitude", "Longitude"], axis=1).groupby(
    ['Station', 'tod', 'dow']).mean().round().reset_index()


a_naive = train_area.drop(["date", "trend", "Latitude", "Longitude"], axis=1).groupby(
    ['area', 'tod', 'dow']).mean().round().reset_index()


g_naive = train_global.drop(["date", "trend"], axis=1).groupby(
    ['tod', 'dow']).mean().round().reset_index()


print("Step 4/4: Output prediction")

format_submission(s_naive, a_naive, g_naive, test_station)

print("Completed! Your submission sample is named sample_result_submission.zip, feel free to upload it directly to the leaderboard!")
