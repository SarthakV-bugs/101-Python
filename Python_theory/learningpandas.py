import pandas as pd


    #to deal with tabular data, rows and columns
    #zero based index
    #Dataframe-consists of different types of data in the table
    #Every column of the dataframe is referred to as SERIES
    #filter - filtering the dataframe
    #
    #CRUD operation -                                                                                                      create, read, update amd delete

def pandasops():

    df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Pincode": [76305, 43284, 98765,],
            "Sex": ["male", "male", "female"],
        }
    )
    print(df)

    print(df["Age"])


    #regex
    '''1. Mathc
       2. Findall
       3. search
    '''

pandasops()