# %%
import pandas as pd
from matplotlib import pyplot as plt
# %%
hours = [0, 4, 8, 12, 16, 20]
meter_1 = [2.1, 2.4, 5.8, 6.2, 5.1, 3.0]

plt.plot(hours, meter_1)
plt.show()
# %%
meter_2 = [1.8, 2.0, 4.9, 7.1, 4.3, 2.5]

plt.plot(hours, meter_1, label='meter_1')
plt.plot(hours, meter_2, label='meter_2')
plt.xlabel('Hour of day')
plt.ylabel('Flow rate (L/min)')
plt.title('Water flow over a day')
plt.legend()

plt.show()
# %%
plt.plot(hours, meter_1, color='#5a7d9a', linestyle='--', marker='o', linewidth=2, label='METER_001')
plt.plot(hours, meter_2, color='#e07b39', linestyle='-', marker='s', linewidth=2, label='METER_002')
plt.xlabel('Hour of day')
plt.ylabel('Flow rate (L/min)')
plt.title('Water flow over a day')
plt.legend()
plt.show()
# %%
plt.style.use('fivethirtyeight')
plt.plot(hours, meter_1, color='#5a7d9a', linestyle='--', marker='o', linewidth=2, label='METER_001')
plt.plot(hours, meter_2, color='#e07b39', linestyle='-', marker='s', linewidth=2, label='METER_002')
plt.xlabel('Hour of day')
plt.ylabel('Flow rate (L/min)')
plt.title('Water flow over a day')
plt.legend()
plt.show()
# %%
plt.grid(True)
plt.tight_layout()
plt.show()
# %%
df = pd.read_csv('/Users/yousefshanti/Desktop/flowless-ai-training/phase-2/module-1/water_meter_readings.csv')

totals = df.groupby('Meter_ID')['Water_Volume'].sum()
totals
# %%
plt.bar(totals.index, totals.values)

plt.xlabel('Meter')
plt.ylabel('Total water volume')
plt.title('Total consumption per meter')
plt.tight_layout()
plt.show()
# %%
plt.barh(totals.index, totals.values)
plt.xlabel('Total water volume')
plt.ylabel('Meter')
plt.show()
# %%
import numpy as np

meters = totals.index
x = np.arange(len(meters))
width = 0.4

avg = df.groupby('Meter_ID')['Water_Volume'].mean()

plt.bar(x - width/2, totals.values, width, label='Total')
plt.bar(x + width/2, avg.values, width, label='Average')

plt.xticks(x, meters)
plt.legend()
plt.tight_layout()
plt.show()
# %%


plt.pie(totals.values, labels=totals.index)
plt.title('Consumption share per meter')
plt.tight_layout()
plt.show()
# %%
plt.pie(totals.values, labels=totals.index, autopct='%1.1f%%')
plt.show()
# %%
explode = [0, 0, 0.1, 0, 0.1]

plt.pie(totals.values, labels=totals.index, explode=explode, autopct='%1.1f%%')
plt.show()
# %%
colors = ['#5a7d9a', '#e07b39', '#7fa874', '#c94f4f', '#9b7fb0']

plt.pie(
    totals.values,
    labels=totals.index,
    autopct='%1.1f%%',
    colors=colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
plt.show()
# %%
meter_3 = [1, 1, 2, 3, 2, 1]

plt.stackplot(hours, meter_1, meter_2, meter_3, labels=['METER_001', 'METER_002', 'METER_003'])

plt.legend(loc='upper left')
plt.title('Total consumption over time by meter')
plt.tight_layout()
plt.show()
# %%
df['DateTime'] = pd.to_datetime(df['DateTime'])

pivot = df.pivot_table(index='DateTime', columns='Meter_ID', values='Water_Volume', aggfunc='sum')
pivot = pivot.fillna(0)

plt.stackplot(pivot.index, pivot.T, labels=pivot.columns)

plt.legend(loc='upper left')
plt.xlabel('Time')
plt.ylabel('Water volume')
plt.title('Stacked consumption per meter over time')
plt.tight_layout()
plt.show()
# %%
df['DateTime'] = pd.to_datetime(df['DateTime'])

m1 = df[df['Meter_ID'] == 'METER_001'].sort_values('DateTime')
m1
# %%
plt.plot(m1['DateTime'], m1['Flow_Rate'])
plt.fill_between(m1['DateTime'], m1['Flow_Rate'], alpha=0.25)

plt.tight_layout()
plt.show()
# %%
threshold = 3

plt.plot(m1['DateTime'], m1['Flow_Rate'])

plt.fill_between(
    m1['DateTime'], m1['Flow_Rate'], threshold,
    where=(m1['Flow_Rate'] > threshold),
    color='red', alpha=0.3, label='Above threshold'
)

plt.axhline(threshold, color='gray', linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()
# %%
m2 = df[df['Meter_ID'] == 'METER_002'].sort_values('DateTime')

plt.plot(m1['DateTime'], m1['Flow_Rate'], label='METER_001')
plt.plot(m2['DateTime'], m2['Flow_Rate'].values, label='METER_002')

plt.fill_between(
    m1['DateTime'], m1['Flow_Rate'], m2['Flow_Rate'].values,
    where=(m1['Flow_Rate'].values > m2['Flow_Rate'].values),
    alpha=0.2, color='green'
)

plt.legend()
plt.tight_layout()
plt.show()
# %%
plt.hist(df['Flow_Rate'])

plt.xlabel('Flow rate (L/min)')
plt.ylabel('Number of readings')
plt.title('Distribution of flow rate')
plt.tight_layout()
plt.show()
# %%
mean_flow = df['Flow_Rate'].mean()

plt.hist(df['Flow_Rate'], bins=20, edgecolor='black')
plt.axvline(mean_flow, color='red', linestyle='--', label=f'Mean = {mean_flow:.1f}')

plt.legend()
plt.tight_layout()
plt.show()
# %%
plt.scatter(df['Pressure'], df['Flow_Rate'])

plt.xlabel('Pressure')
plt.ylabel('Flow rate (L/min)')
plt.title('Pressure vs flow rate')
plt.tight_layout()
plt.show()
# %%
plt.scatter(df['Pressure'], df['Flow_Rate'], s=50, c='green', marker='o', edgecolor='black', alpha=0.6)
plt.show()
# %%
plt.scatter(df['Pressure'], df['Flow_Rate'], c=df['Temperature'], cmap='viridis')

cbar = plt.colorbar()
cbar.set_label('Temperature')

plt.xlabel('Pressure')
plt.ylabel('Flow rate (L/min)')
plt.tight_layout()
plt.show()
# %%
plt.scatter(df['Pressure'], df['Flow_Rate'], c=df['Temperature'], cmap='viridis', s=df['Water_Volume'])
plt.colorbar(label='Temperature')
plt.show()
# %%
df['DateTime'] = pd.to_datetime(df['DateTime'])

m1 = df[df['Meter_ID'] == 'METER_001'].sort_values('DateTime')

plt.plot(m1['DateTime'], m1['Flow_Rate'])
plt.tight_layout()
plt.show()
# %%
plt.plot(m1['DateTime'], m1['Flow_Rate'])

plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()
# %%

m1_daily = m1.set_index('DateTime')['Flow_Rate'].resample('D').mean()

plt.plot(m1_daily.index, m1_daily.values)
plt.title('Daily average flow — METER_001')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()
# %%
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

ax1.plot(df['DateTime'], df['Flow_Rate'], label='Flow')
ax1.set_title('Flow rate over time')
ax1.set_xlabel('Time')
ax1.set_ylabel('Flow')
ax1.legend()

ax2.plot(df['DateTime'], df['Pressure'], label='Pressure')
ax2.set_title('Pressure over time')
ax2.legend()

plt.tight_layout()
plt.show()
# %%
fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0, 0].plot(df['DateTime'], df['Flow_Rate'])
axes[0, 1].hist(df['Flow_Rate'])
axes[1, 0].scatter(df['Pressure'], df['Flow_Rate'])
axes[1, 1].bar(df['Meter_ID'].unique(), df.groupby('Meter_ID')['Water_Volume'].sum())

plt.tight_layout()
plt.show()
