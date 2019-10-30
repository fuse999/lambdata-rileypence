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

    def __init__(self, df):
      self.dataframe = df


    def getcsv(data_url):
        return(pd.read_csv(data_url))  # This is a test function for myself.

    def display_num(self):
      """
      This function Shows all # with a describe function
      """
        return(self.df.select_dtypes(include='number').describe().T)

    def display_non_num(self):
      """
      This function shows all non numerical columns
      from dataframe in order by unique values
      """
        return(self.df.select_dtypes(exclude='number')
                 .describe().T.sort_values(by='unique'))

    def split_df(self):
      """
      easy preset train test split
      """
        train, test = train_test_split(self.df, test_size=0.30, random_state=59)
        print("split_df has returned 'train' and 'test' dataframes.")
        return(train, test)

    def remove_outlier(self, col_name):
        q1 = self.df[col_name].quantile(0.25)
        q3 = self.df[col_name].quantile(0.75)
        iqr = q3-q1  # Interquartile range
        fence_low = q1-1.5*iqr
        fence_high = q3+1.5*iqr
        df_out = self.df.loc[(self.df[col_name] > fence_low) &
                           (self.df[col_name] < fence_high)]
        return(df_out)