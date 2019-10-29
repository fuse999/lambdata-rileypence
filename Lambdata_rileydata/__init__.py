"""
lambdata-rileypence - A colection Of basic functions
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

# Sample Dataset
bobdata = {'id': [0, 1, 2], 'Quantity': [1, 1, 1], 'Item Name':['Backpack', 'Camp Knife', 'Ferrocenium Rod'], 'Price':[45.99, 7.70, 9.98], 'Purchased':[True, False, True], 'Url':["https://www.amazon.com/gp/product/B01B76LV4O/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1", "https://www.amazon.com/dp/B01K27GPUE/ref=twister_B0728J49TM?_encoding=UTF8&psc=1", "https://www.amazon.com/gp/product/B00S6F4RDC/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1"]}
bobdata = pd.DataFrame(data=bobdata)

# Sample Function
def read_view_csv(url):
    df = pd.read_csv(url)
    print(df.head(5))
    return(df)

def cust_split(X):
    train, test = train_test_split(X,test_size=0.2, random_state=59)
    return(train, test)