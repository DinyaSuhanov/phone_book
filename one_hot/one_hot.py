
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# приводим к виду one_hot

data = pd.DataFrame({'whoAmi': lst})
data.loc[data['whoAmi'] == 'robot', 'c_rob'] = '1'
data.loc[data['whoAmi'] != 'robot', 'c_rob'] = '0'
data.loc[data['whoAmi'] == 'human', 'c_hum'] = '1'
data.loc[data['whoAmi'] != 'human', 'c_hum'] = '0'

print(data.head(n=10))