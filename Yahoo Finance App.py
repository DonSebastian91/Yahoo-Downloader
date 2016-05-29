
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas_datareader import data, wb
import datetime as dt


# In[2]:

date_start = input('Enter a start date (YYYY-MM-DD): ')
year, month, day = map(int, date_start.split('-'))
start = dt.date(year, month, day)

date_end = input('Enter an end date (YYYY-MM-DD): ')
year, month, day = map(int, date_end.split('-'))
end = dt.date(year, month, day)


# In[3]:

df = data.DataReader("AAPL", 'yahoo', start, end)


# In[4]:

df.to_csv('Yahoo_Data')

