# %%
from statistics import mean

import pandas as pd
pd.DataFrame(
    {'Bob': ['I liked it.', 'It was awful.'],
     'Sue': ['Pretty good.', 'Bland.']},
    index=['Product A', 'Product B']
)
# %%
pd.Series([1, 2, 3, 4, 5])
# %%
pd.Series([30, 35, 40],
          index=['2015 Sales', '2016 Sales', '2017 Sales'],
          name='Product A')
# %%
df = pd.read_csv("water_meter_readings.csv")
# %%
df.shape
# %%
df.head()
# %%
df['Meter_ID']
# %%
df['Meter_ID'][0]
# %%
df.iloc[0]
# %%
df.iloc[:, 0]
# %%
df.iloc[:3, 0]
# %%
df.iloc[[0, 4, 2], 0]
# %%
df.loc[0, 'Meter_ID']
# %%
df.Meter_ID == 'METER_003'
# %%
df.iloc[(df.Meter_ID == 'METER_003')&(df.Flow_Rate<2)]
# %%
df['index_backwards'] = range(len(df), 0, -1)
# %%
df.head()
# %%
df.iloc[df.Flow_Rate<1]
# %%
df.Meter_ID.describe()
# %%
df.Meter_ID.unique()
# %%
df.Meter_ID.value_counts()
# %%
df.loc[df.Flow_Rate.idxmax()]
# %%
df.Flow_Rate - df.Flow_Rate.mean()
# %%
df.Flow_Rate.map(lambda x: x  - df.Flow_Rate.mean())
# %%
df.groupby('Meter_ID').Flow_Rate.mean()
# %%
df.groupby('Meter_ID').Flow_Rate.sum()
# %%
df.groupby('Meter_ID').Flow_Rate.max()
# %%
df.groupby('Meter_ID').Flow_Rate.count()
# %%
df.groupby('Meter_ID').Flow_Rate.agg(['sum', 'mean', 'max'])
# %%
consumption = df.groupby('Meter_ID').Flow_Rate.sum().reset_index()
# %%
consumption.sort_values(by='Flow_Rate', ascending=False)
# %%
df.sort_values(by='Flow_Rate', ascending=True)
# %%
df.dtypes
# %%
df.isnull().sum()
# %%
df[df.Flow_Rate.isnull()]
# %%
df.rename(columns={'Flow_Rate': 'Flow Rate'})
# %%
df.dtypes
