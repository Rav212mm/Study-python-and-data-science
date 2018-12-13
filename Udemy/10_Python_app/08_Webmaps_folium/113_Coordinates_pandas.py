import pandas as pd

col_list = ['NAME', 'LOCATION','LAT', 'LON']
df = pd.read_csv('Volcanoes.txt', usecols=col_list)
print(df.head())
vol_loc = df

LAT = list(df['LAT'])
LON = list(df['LON'])
COMMENT = list(df['NAME'] + ',' + df['LOCATION'])

print(len(LAT), len(LON), len(COMMENT))

print(COMMENT)
k = list(zip(LAT, LON, COMMENT))

for i in range(4):
    print(k[i])