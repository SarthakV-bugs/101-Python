import pandas as pd

cricket_analytics = pd.read_json("/home/ibab/PYTHON_LAB/Lab28/ODI-Batting_Cricket_Analytics.json")

#a
print(cricket_analytics.columns.tolist())

#b
sorted_score = cricket_analytics.sort_values(by='ScoreRate', ascending=False).head(5)
print(sorted_score['Player'])

#c
print(cricket_analytics[cricket_analytics['Runs'] == cricket_analytics['Runs'].min()]['Player'])

# #d
print(cricket_analytics['Runs'].value_counts()[cricket_analytics['Runs'].min()])

# #e
avg_runs = cricket_analytics['Runs'].mean()
print(cricket_analytics[(cricket_analytics['Country'] == 'India') & (cricket_analytics['Runs'] > avg_runs)]['Player'])