import pandas as pd
import numpy as np
df1 = pd.read_csv('actual.txt', sep="|", names=['time','stock','price'])
df2 = pd.read_csv('predicted.txt', sep="|", names=['time1','stock1','price1'])
print (df1.dtypes)
size = open('window.txt', 'r').read()
print (size)
df3 = pd.merge(df1, df2, how='inner', left_on = ['time','stock'], right_on = ['time1','stock1'])
df3['error'] = abs (df3['price'] - df3 ['price1'])
df4 = pd.DataFrame(columns=['time1','time2','meanerror'])
for i in range (1, df3['time'].max()):
    window = i + int(size)
    array = range (i,window)
    df3_window = df3.loc[df3['time'].isin(array)]
    meanerr = round (df3_window["error"].mean(), 2)
    s = pd.Series([i, window, meanerr], index=['time1', 'time2', 'meanerror'])
    #print (s)
    df4 = df4.append(s, ignore_index=True)
df4.time1 = df4.time1.astype(int)
df4.time2 = df4.time2.astype(int)
#df4["time2"] = pd.to_numeric(df4["time2"])
print (df4)
df4.to_csv(r'output.txt', header=None, index=None, sep=' ')
