# http://www.woshipm.com/operate/1295461.html
import os
import sys
import datetime
import numpy as np
import pandas as pd

def count_days(time_ago):
    return (datetime.datetime.now() - time_ago).days

def user_segment(row):
    return {(True, True, True): 1,  # 重要价值用户
            (True, False, True): 2, # 重要发展用户
            (False, True,  True): 3, # 重要保持用户
            (False, False,  True): 4, # 重要挽留用户
            (True, True, False): 5, # 一般价值用户
            (True, False, False): 6, # 一般发展用户
            (False, True, False): 7, # 一般保持用户
            (False, False, False): 8, # 一般挽留用户
           }[(row['R'], row['F'], row['M'])] 


df = pd.read_excel('./2019-12-24.xlsx', dtype={'pay_time': np.datetime64}) 
df['recency'] =  df['pay_time'].apply(count_days)

print('df.median is ', df.median())

df['R'] = (df['recency'] <= df['recency'].median())
df['F'] = (df['count'] >= df['count'].median())
df['M'] = (df['sum( amount )'] >= df['sum( amount )'].median())
df['user_segment'] = df.apply(user_segment, axis=1)
df = df[['uid', 'pay_time', 'count', 'sum( amount )', 'R', 'F', 'M', 'user_segment']]

print('df.shape is ', df.shape)
print('df.dtypes is ', df.dtypes)
print('df.head(10) is ', df.head(10))
df.to_excel('./user_segmentation.xlsx', index=False)

print('prog ends here!')
sys.exit(0)

#######################################################################################

del df['pay_time']

time_ago = datetime.datetime.strptime("2019-12-01 1:20:30", "%Y-%m-%d %H:%M:%S")
print('count_days is ', count_days(time_ago))
#sys.exit(0)
