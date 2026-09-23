# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/yousefshanti/Desktop/flowless-ai-training/phase-2/module-1/water_meter_readings.csv')
df['DateTime'] = pd.to_datetime(df['DateTime'])
df = df.sort_values('DateTime')

meters = df['Meter_ID'].unique()
totals = df.groupby('Meter_ID')['Water_Volume'].sum()
# %%
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16, 9))
fig.suptitle('Water Meter Readings — EDA Dashboard', fontsize=16)

for meter in meters:
    m = df[df['Meter_ID'] == meter]
    axes[0, 0].plot(m['DateTime'], m['Water_Volume'], label=meter)

axes[0, 0].set_title('Consumption trends over time (Line)')
axes[0, 0].set_xlabel('Time')
axes[0, 0].set_ylabel('Water volume')
axes[0, 0].legend(fontsize=8)
axes[0, 0].tick_params(axis='x', rotation=45)

axes[0, 1].bar(totals.index, totals.values, color='#5a7d9a')
axes[0, 1].set_title('Meter comparison — total volume (Bar)')
axes[0, 1].set_xlabel('Meter')
axes[0, 1].set_ylabel('Total volume')
axes[0, 1].tick_params(axis='x', rotation=45)

axes[0, 2].pie(totals.values, labels=totals.index, autopct='%1.1f%%')
axes[0, 2].set_title('Meter comparison — consumption share (Pie)')


pivot = df.pivot_table(index='DateTime', columns='Meter_ID', values='Water_Volume', aggfunc='sum').fillna(0)
axes[1, 0].stackplot(pivot.index, pivot.T, labels=pivot.columns)
axes[1, 0].set_title('Consumption trends over time (Stack)')
axes[1, 0].set_xlabel('Time')
axes[1, 0].set_ylabel('Water volume')
axes[1, 0].legend(fontsize=8, loc='upper left')
axes[1, 0].tick_params(axis='x', rotation=45)

axes[1, 1].hist(df['Flow_Rate'], bins=15, edgecolor='black', color='#7fa874')
axes[1, 1].set_title('Flow rate distribution (Histogram)')
axes[1, 1].set_xlabel('Flow rate')
axes[1, 1].set_ylabel('Number of readings')

q_hi = df['Flow_Rate'].quantile(0.95)
normal = df[df['Flow_Rate'] <= q_hi]
anomaly = df[df['Flow_Rate'] > q_hi]

axes[1, 2].scatter(normal['Pressure'], normal['Flow_Rate'], alpha=0.6, color='#7fa874', label='Normal')
axes[1, 2].scatter(anomaly['Pressure'], anomaly['Flow_Rate'], color='red', label='Anomaly')
axes[1, 2].set_title('Highlight anomalies — pressure vs flow rate (Scatter)')
axes[1, 2].set_xlabel('Pressure')
axes[1, 2].set_ylabel('Flow rate')
axes[1, 2].legend(fontsize=8)

plt.tight_layout()
plt.show()

fig.savefig('eda_dashboard.png', dpi=300, bbox_inches='tight')
