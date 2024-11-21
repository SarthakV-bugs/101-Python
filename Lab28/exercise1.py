# https://numpy.org/devdocs/user/quickstart.html

import numpy as np
import pandas as pd


def numpy_exercises():

    print(np.__version__)

    # How to create a 1D array?
    x = np.arange(10)
    print(x)

    # How to create a boolean array?
    print(np.ones((3, 3), dtype=bool))

    # How to extract items that satisfy a given condition from 1D array
    arr = np.arange(10)
    print(arr[arr % 2 == 1])

    # How to replace items that satisfy a condition with another value in numpy array
    # Replace all odd numbers in arr with -1
    arr = np.arange(10)
    arr[arr % 2 == 1] = -1
    print(arr)

    # How to replace items that satisfy a condition without affecting the original array
    arr = np.arange(10)
    out = arr.copy()
    out[out % 2 == 1] = -1
    print(out)

    # How to reshape an array?
    arr = np.arange(10)
    print(arr.reshape(2, 5))

    # How to stack two arrays vertically?
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)
    print(np.vstack([a, b]))

    # How to stack two arrays horizontally?
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)
    print(np.hstack([a,b]))

    # How to get the common items between two python numpy arrays?
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    print(np.intersect1d(a, b))

    # How to remove from one array those items that exist in another
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 6, 7, 8, 9])
    print(np.setdiff1d(a, b))

    # How to get the positions where elements of two arrays match?
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    print(np.where(a == b))

    # How to extract all numbers between a given range from a numpy array?
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    print(a[(a >= 5) & (a <= 10)])

    #  How to make a python function that handles scalars to work on numpy arrays?
    def maxx(x, y):
        """Get the maximum of two items"""
        if x >= y:
            return x
        else:
            return y

    def pair_max(x, y):
        # using zip
        maximum = [maxx(a,b) for a,b in zip(x,y)]
        return np.array(maximum)

    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])
    print(pair_max(a, b))

    # How to swap two columns in a 2d numpy array?
    arr = np.arange(9).reshape(3, 3)
    print(arr)
    new_arr = arr[:, [1, 0, 2]]
    print(new_arr)

    # How to swap two rows in a 2d numpy array?
    arr = np.arange(9).reshape(3, 3)
    new_arr = arr[[1,0,2], :]
    print(new_arr)

    # How to reverse the rows of a 2D array?
    arr = np.arange(9).reshape(3, 3)
    print(arr)

    new_arr = arr[::-1, :]
    print(new_arr)


    # How to create a 2D array containing random floats between 5 and 10?¶
    rand_arr = np.random.uniform(5, 10, size=(5, 3))
    print(rand_arr)

    # How to print only 3 decimal places in python numpy array?
    rand_arr = np.random.random((5, 3))
    np.set_printoptions(precision=3)
    print(rand_arr)

    # How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
    np.random.seed(100)
    rand_arr = np.random.random([3, 3]) / 1e3
    np.set_printoptions(suppress=False)
    print(rand_arr)
    np.set_printoptions(suppress=True)
    print(rand_arr)

    # compute mean, median and standard deviation of a numpy array
    # How to normalize an array so the values range exactly between 0 and 1?  # (data - min)/(max - min)
    # How to filter a numpy array based on two or more conditions?
    iris_data = np.genfromtxt('/home/ibab/PYTHON_LAB/lab28/Iris.csv', delimiter=',', dtype='float', usecols=[1, 2, 3, 4],
                              skip_header=1)
    print(iris_data[(iris_data[:, 2] > 1.5) & (iris_data[:, 0] < 5.0)])
#

    # How to find the correlation between two columns of a numpy array?
    diabetes_data = np.genfromtxt('/home/ibab/PYTHON_LAB/lab28/diabetes.csv',
                                  delimiter=',', dtype='float', usecols=[0, 1, 2, 3, 4, 5, 6, 7], skip_header=1)
#
    print(np.corrcoef(diabetes_data[:, 1], diabetes_data[:, 5]))
#
    print('\n')
    # you can get correlation by getting value at index [0,1] or [1,0]
    print(np.corrcoef(diabetes_data[:, 1], diabetes_data[:, 5])[0, 1])
#
    # How to find if a given array has any null values?
    # question: Find out if iris_2d has any missing values.
    diabetes_data = np.genfromtxt('/home/ibab/PYTHON_LAB/lab28/diabetes.csv',
                                  delimiter=',', dtype='float', usecols=[0, 1, 2, 3, 4, 5, 6, 7], skip_header=1)

    print(np.isnan(diabetes_data).any())

      # How to replace all missing values with 0 in a numpy array?
    wine_quality = np.genfromtxt('/home/ibab/PYTHON_LAB/lab28/winequality-red.csv',
                                 delimiter=',', dtype='float', usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 skip_header=1)

    wine_quality[np.random.randint(len(wine_quality), size=20), np.random.randint(11, size=20)] = np.nan

    print("Does dataset have any Nan value:", np.isnan(wine_quality).any())

    wine_quality[np.isnan(wine_quality)] = 0

    print("Does dataset have any Nan value:", np.isnan(wine_quality).any())

    # How to find the count of unique values in a numpy array?
    # mushroom = np.genfromtxt('../input/mushroom-classification/mushrooms.csv',
    #                          delimiter=',', dtype=object, usecols=[0], skip_header=1)
    # # mushroom
    # np.unique(mushroom, return_counts=True)

def pandas_exercises():
    import datetime

    df_data = pd.read_json("/home/ibab/PYTHON_LAB/lab28/ODI-Batting_Cricket_Analytics.json")
    print(df_data.shape)

# What is the year range when all matches were played?

    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    print(f"Starting year {df_match_date.min()} , Ending year {df_match_date.max()}")

 # How many matches does India play?
    df_data_india = df_data[df_data["Country"] == "India"]
    num_matches = len(df_data_india)
    print("Number of India matches = ", num_matches)

# How many matches does India play after year 2000?
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    date_2000 = pd.to_datetime('1/1/2000')
    df_data_india_2000 = df_data[(df_data["Country"] == "India")  & (df_match_date > date_2000)]
    num_matches = len(df_data_india_2000)
    print("Number of India matches after the Year 2000 = ", num_matches)

    # who is the top scorer for India in the year 2010
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    start_date = pd.to_datetime('1/1/2010')
    end_date = pd.to_datetime('1/1/2011')
    df_matches = df_data[(df_data["Country"] == "India") & (df_match_date > start_date ) & (df_match_date < end_date)]
    num_matches = len(df_matches)
    print("Number of India matches = ", num_matches)
    df_player_scores = df_matches.groupby(["Player"])["Runs"].sum()
    print(f"Player {df_player_scores.idxmax()}, Total Runs {df_player_scores.max()}")

    # List the top 5 scorers in the year 2010
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    start_date = pd.to_datetime('1/1/2010')
    end_date = pd.to_datetime('1/1/2011')
    df_matches = df_data[(df_match_date > start_date ) & (df_match_date < end_date)]
    num_matches = len(df_matches)
    print("Number of matches = ", num_matches)
    df_player_scores = df_matches.groupby(["Player"])["Runs"].sum()
    s_sorted = df_player_scores.sort_values(ascending=False)
    print("Top 5 players")
    print(s_sorted.head())

    # check

    # What is the average score of each Indian player played in the year 2010
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    start_date = pd.to_datetime('1/1/2010')
    end_date = pd.to_datetime('1/1/2011')
    df_matches = df_data[(df_data["Country"] == "India") & (df_match_date > start_date ) & (df_match_date < end_date)]
    num_matches = len(df_matches)
    print("Number of India matches = ", num_matches)
    df_player_scores = df_matches.groupby(["Player"])["Runs"].mean()
    print(df_player_scores)

    # how many matches India played against each country in the year 2010
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    start_date = pd.to_datetime('1/1/2010')
    end_date = pd.to_datetime('1/1/2011')
    df_matches = df_data[(df_data["Country"] == "India") & (df_match_date > start_date) & (df_match_date < end_date)]
    df_india_matches = df_matches.groupby(["Versus"])
    print(df_india_matches['Versus'].value_counts())


def main():

    numpy_exercises()

    pandas_exercises()

if __name__ == "__main__":
        main()