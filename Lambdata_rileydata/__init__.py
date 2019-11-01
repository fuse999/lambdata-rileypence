"""
lambdata-rileypence - A colection Of basic functions and data
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

# Sample Dataset
bobdata = {'id': [0, 1, 2], 'Quantity': [1, 1, 1], 'Item Name':['Backpack', 'Camp Knife', 'Ferrocenium Rod'], 'Price':[45.99, 7.70, 9.98], 'Purchased':[True, False, True], 'Url':["https://www.amazon.com/gp/product/B01B76LV4O/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1", "https://www.amazon.com/dp/B01K27GPUE/ref=twister_B0728J49TM?_encoding=UTF8&psc=1", "https://www.amazon.com/gp/product/B00S6F4RDC/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1"]}
bobdata = pd.DataFrame(data=bobdata)
# Sample lists
ONES = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ZEROS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Test variable
TEST_VAR = 9
# Sample Function
def incrment_1(x):
    """This adds one to input value"""
    return(x + 1)

def mult2(x):
    """This adds one to input value"""
    return(x * 2)