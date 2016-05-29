import numpy as np
import pandas as pd
from pandas_datareader import data, wb
import datetime as dt

# Get dates and make sure datetime can use them
date_start = input('Enter a start date (YYYY-MM-DD): ')
year, month, day = map(int, date_start.split('-'))
start = dt.date(year, month, day)

date_end = input('Enter an end date (YYYY-MM-DD): ')
year, month, day = map(int, date_end.split('-'))
end = dt.date(year, month, day)

# Get yahoo finance data
df = data.DataReader("AAPL", 'yahoo', start, end)

# Convert to CSV
df.to_csv('Yahoo_Data')
