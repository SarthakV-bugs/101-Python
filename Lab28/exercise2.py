import pandas
import pandas as pd


# def main():

df = pd.read_csv("/home/ibab/PYTHON_LAB/Lab28/diabetes.csv")


#A)
print(df.columns.tolist())

#B)
print(df.head(10))

#C)
print(df['BloodPressure'].mean())

#D)
print(df.iloc[0:4,2:5])

#E)
df['NormalizedBP'] = (df['BloodPressure'].min()) / (df['BloodPressure'].max()) - (df['BloodPressure'].max() - (df['BloodPressure'].min()))
print(df["NormalizedBP"])


#F)
def cat_age(age):
    if 1 <= age <= 18:
        return "Youth"
    elif 19 <= age <= 50:
        return "Adult"
    elif age > 50:
        return "Senior"
    else:
        return "Invalid age bracket!"

df['age_category'] = df['Age'].apply(cat_age)
print(df['age_category'])