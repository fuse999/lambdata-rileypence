"""
Utility functions for working with DF
"""
# Imports to work with pandas dataframe
import pandas as pd
from sklearn.model_selection import train_test_split

class Df_Preper:
    """
    Pandas dataframe Cleaning tools
    """

    def getcsv(data_url):
        return(pd.read_csv(data_url))  # This is a test function for myself.

    def display_num(df):
      """
      This function Shows all # with a describe function
      """
        return(df.select_dtypes(include='number').describe().T)

    def display_non_num(df):
      """
      This function shows all non numerical columns
      from dataframe in order by unique values
      """
        return(df.select_dtypes(exclude='number')
                 .describe().T.sort_values(by='unique'))

    def split_df(df):
      """
      easy preset train test split
      """
        train, test = train_test_split(df, test_size=0.30, random_state=59)
        print("split_df has returned 'train' and 'test' dataframes.")
        return(train, test)

    def remove_outlier(df_in, col_name):
        q1 = df_in[col_name].quantile(0.25)
        q3 = df_in[col_name].quantile(0.75)
        iqr = q3-q1  # Interquartile range
        fence_low = q1-1.5*iqr
        fence_high = q3+1.5*iqr
        df_out = df_in.loc[(df_in[col_name] > fence_low) &
                           (df_in[col_name] < fence_high)]
        return(df_out)