import pandas as pd
#
# def pandasops():
#     # A dataframe is a 2-D data structure that can store data of different types in columns
#     # It is similar to a spreadsheet or SQL table
#     # Each column in a dataframe is a series
#
df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Pincode": [76305, 43284, 98765],
            "Sex": ["male", "male", "female"],
        }
    )
print(df)





   #### Each column in a dataframe is a series
print(df["Age"])

   # # create a series from scratch
newages = pd.Series([22, 35, 58], name="NewAge")
print(newages)

#
#     # get the maximum age of passengers
#     print(df["Age"].max())
#
#     # basic statistics about the dataframe
#     # The describe() method provides a quick overview of the numerical data in a DataFrame.
#     # As the Name and Sex columns are textual data, these are by default not taken into account by the describe() method.
#     print(df.describe())
#
#     # reading a file
#     titanic = pd.read_csv("~/ibab-repo/titanic.csv")
#     print(titanic)
#     print(titanic.head(8))
#     print(titanic.tail(8))
#     print(titanic.dtypes)
#     # save as xlsx
#     import openpyxl
#     titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
#
#     # pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …),
#     # each of them with the prefix read_*.
#     titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
#     print(titanic)
#     print(titanic.info())
#
#     # selecting a subset of a dataframe
#     print(titanic["Age"])
#     print(titanic["Age"].shape)
#     age_sex = titanic[["Age", "Sex"]]
#     print(age_sex)
#     print(age_sex.shape)
#
#     # filter specific rows
#     above_35 = titanic[titanic["Age"] > 35] # passengers older than 35 yrs
#     class_23 = titanic[titanic["Pclass"].isin([2, 3])] # Titanic passengers from cabin class 2 and 3.
#     # use of | and & operator
#     class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)] # same as above
#     # passenger data for which the age is known
#     age_no_na = titanic[titanic["Age"].notna()]
#     print(age_no_na.shape)
#     # selecting specific rows and columns
#     # When using loc/iloc, the part before the comma is the rows you want, and the part after the comma is the columns you want to select.
#     adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
#     # rows 10 till 25 and columns 3 to 5.
#     print(titanic.iloc[9:25, 2:5])
#     # assign the name anonymous to the first 3 elements of the fourth column
#     titanic.iloc[0:3, 3] = "anonymous"
#
#     ### plots in pandas
#     import matplotlib.pyplot as plt
#     # The usage of the index_col and parse_dates parameters of the read_csv function to define the
#     # first (0th) column as index of the resulting DataFrame and convert the dates in the column to Timestamp
#     # objects, respectively.
#     air_quality = pd.read_csv("~/ibab-repo/air_quality_no2.csv", index_col=0, parse_dates=True)
#     print(air_quality)
#     # With a DataFrame, pandas creates by default one line plot for each of the columns with numeric data.
#     air_quality.plot()
#     plt.show()
#     # plot only the columns of the data table with the data from Paris.
#     air_quality["station_paris"].plot()
#     plt.show()
#     # scatter
#     air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
#     plt.show()
#     # ['area', 'bar', 'barh', 'box', 'density', 'hexbin', 'hist', 'kde', 'line', 'pie', 'scatter']
#     # box plot
#     air_quality.plot.box()
#     plt.show()
#     # each of the columns in a separate subplot. Separate subplots for each of the data columns are
#     # supported by the subplots argument of the plot functions.
#     xs = air_quality.plot.area(figsize=(12, 4), subplots=True)
#     plt.show()
#
#     ### create new columns derived from existing columns
#     # To create a new column, use the [] brackets with the new column name at the left side of the assignment.
#     # The calculation of the values is done element-wise. This means all values in the given column
#     # are multiplied by the value 1.882 at once. You do not need to use a loop to iterate each of the rows!
#     air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
#     print(air_quality.head())
#     # ratio of the values in Paris versus Antwerp and save the result in a new column.
#     air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])
#     # rename the data columns to the corresponding station identifiers
#     air_quality_renamed = air_quality.rename(columns={"station_antwerp": "BETR801",
#                                                       "station_paris": "FR04014",
#                                                       "station_london": "London Westminster"})
#     print(air_quality_renamed.head())
#
#     ### Summary statistics
#     # average age of the Titanic passengers?
#     print(titanic["Age"].mean())
#     # Different statistics are available and can be applied to columns with numerical data.
#     # Operations in general exclude missing data and operate across rows by default.
#     # median age and ticket fare price of the Titanic passengers?
#     print(titanic[["Age", "Fare"]].median())
#     # diff stats
#     print(titanic[["Age", "Fare"]].describe())
#     print(titanic.agg({
#                         "Age":["min", "max", "median", "skew"],
#                         "Fare":["min", "max", "median", "mean"],
#     })
#     )
#
#     ### groupby
#     df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'],
#                        'Max Speed': [380., 370., 24., 26.]}
#                       )
#     m = df.groupby(['Animal']).mean()
#     print(m)
#
#     # average age for male versus female Titanic passengers?
#     df_s = titanic[["Sex", "Age"]].groupby("Sex")
#     print(df_s.mean())
#     print(df_s.mean(numeric_only=True))
#     print(df_s["Age"].mean())
#     # mean ticket fare price for each of the sex and cabin class combinations?
#     # Grouping can be done by multiple columns at the same time. Provide the column names
#     # as a list to the groupby() method.
#     df_sp = titanic.groupby(["Sex", "Pclass"])
#     print(df_sp["Fare"].mean())
#
#     ### Count number of records by category
#     # number of passengers in each of the cabin classes?
#     print(titanic["Pclass"].value_counts())
#
#     ### reshape the layout of tables
#     # sort the Titanic data according to the age of the passengers.
#     titanic_sorted_age = titanic.sort_values(by="Age").head()
#     print(titanic_sorted_age)
#
#     # sort the Titanic data according to the cabin class and age in descending order.
#     titanic_sorted_pclass_age = titanic.sort_values(by=['Pclass', 'Age'], ascending=False)
#     print(titanic_sorted_pclass_age)
#
#     ### combine data from multiple tables
#     air_quality_no2 = pd.read_csv("~/ibab-repo/air_quality_no2_long.csv",parse_dates=True)
#     air_quality_no2 = air_quality_no2[["date.utc", "location","parameter", "value"]]
#     air_quality_pm25 = pd.read_csv("~/ibab-repo/air_quality_pm25_long.csv",parse_dates=True)
#     air_quality_pm25 = air_quality_pm25[["date.utc", "location","parameter", "value"]]
#     air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
#     print(air_quality)
#
#
#
#     ### Join tables using a common identifier
#     # merge
#     df1 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
#     df2 = pd.DataFrame({'a': ['foo', 'baz'], 'c': [3, 4]})
#     df_inner = df1.merge(df2, how='inner', on='a')
#     df_left = df1.merge(df2, how='left', on='a')
#     df_right = df1.merge(df2, how='right', on='a')
#
#     df1 = pd.DataFrame({'left': ['foo', 'bar']})
#     df2 = pd.DataFrame({'right': [7, 8]})
#     df_cross = df1.merge(df2, how='cross')
#
#
#
#     stations_coord = pd.read_csv("~/ibab-repo/air_quality_stations.csv")
#     print(stations_coord.head())
#     print(air_quality.head())
#     air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
#     print(air_quality.head())
#
#     ###
#     air_quality_parameters = pd.read_csv("~/ibab-repo/air_quality_parameters.csv")
#     print(air_quality_parameters.head())
#     air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
#     print(air_quality)