
from pandas import DataFrame

def add_state_names(my_df):
    new_df = my_df.copy()
    names_map = {"CA":"Cali", "CO":"Colo", "CT":"Conn"}
    new_df["name"] = new_df["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    return new_df

if __name__ == "__main__":

    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
