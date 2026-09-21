# %%
# Load CSV file with water meter data
import pandas as pd
df = pd.read_csv("water_meter_readings.csv")
# %%
df.head()
# %%
df.shape
# %%
df.info()
# %%
df.columns
# %%
# Display sensor information
df['Meter_ID'].unique()
# %%
df['Meter_ID'].nunique()
# %%
df['Meter_ID'].value_counts()
# %%
# Check data types and missing values
df.dtypes
# %%
df.isnull().sum()
# %%
df.describe()
# %%
# duplicate readings
df.duplicated()
# %%
df.duplicated().sum()
# %%
df['Pressure'].std()
# %%
df['Flow_Rate'].mean()
# %%
#Identify outliers using statistical methods (Z-score)
mean = df['Flow_Rate'].mean()
std = df['Flow_Rate'].std()

df[((df['Flow_Rate'] - mean) / std).abs() > 3]
# %%
# the highest flow rate
df.sort_values('Flow_Rate', ascending=False).head(1)
# %%
# the average water temperature for METER_003
df[df['Meter_ID'] == 'METER_003']['Temperature'].mean()
# %%
df['DateTime'] = pd.to_datetime(df['DateTime'])
# %%
# the total water volume for METER_005 on 2024-01-01
mask = (df['Meter_ID'] == 'METER_005') & (df['DateTime'].dt.date == pd.to_datetime('2024-01-01').date())
df[mask]['Water_Volume'].sum()
# %%
#Group data by meter and time periods
df.groupby(['Meter_ID', df['DateTime'].dt.date])['Water_Volume'].sum()
# %%
#Calculate total, average, and peak consumption
df.groupby('Meter_ID')['Water_Volume'].agg(['sum', 'mean', 'max'])
# %%
# Identify Consumption Trends
meter = df[df['Meter_ID'] == 'METER_003']
meter.groupby(meter['DateTime'].dt.date)['Water_Volume'].sum()
# %%
# Consumption Trends for METER_003
meter.groupby(meter['DateTime'].dt.date)['Water_Volume'].sum().plot()
# %%
#Compare meters for anomalies
summary = df.groupby('Meter_ID')[['Flow_Rate', 'Pressure', 'Water_Volume']].mean()
summary
# %%
summary.sort_values('Flow_Rate', ascending=False)
# %%
avg = summary['Flow_Rate'].mean()
std = summary['Flow_Rate'].std()

summary[(summary['Flow_Rate'] > avg + std) | (summary['Flow_Rate'] < avg - std)]
# %%
# more cases here -> Peak hours
df.groupby(df['DateTime'].dt.hour)['Water_Volume'].sum().sort_values(ascending=False).head(5)
# %% [markdown]
# # Water Meter Data — Results Summary
#
# ## Overview
# - 55 readings from 5 meters (11 each)
# - No missing values, no duplicates
# - Period: 2024-01-01 to 2024-01-03
#
# ## Answers
# - Highest flow rate: METER_001 on 2024-01-02
# - Average temperature for METER_003: 15.78
# - Total volume for METER_005 on 2024-01-01: 2230
# - Peak consumption hour: 6 AM
#
# ## Outliers & Anomalies
# - Z-score method: METER_001 had 3 abnormal flow readings on 2024-01-02
#   (above 4.6 vs a normal ~1.5) — possible leak or sensor error
# - By average flow: METER_001 stands out high, METER_004 stands out low
