#! C:\Users\macro.ip\Desktop\Chiller_System\venv\Scripts\python.exe

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

df = pd.read_csv("C:\\Users\\Marco ip\\OneDrive\\Desktop\\Chiller_System\\data_dump.csv") # change string to raw strong
df.head()

count_row = df.shape[0]  # Gives number of rows
count_col = df.shape[1]  # Gives number of columns
C1STemp = df.loc[df['ACPC-1Comp_Power'] > 10, 'ACPC-1CHWS_Temp']
C1RTemp = df.loc[df['ACPC-1Comp_Power'] > 10, 'ACPC-1CHWR_Temp']
C1FRate = df.loc[df['ACPC-1Comp_Power'] > 10, 'ACPC-1Flow_Rate']
C1DTemp = C1STemp - C1RTemp
Timestamp1 = pd.to_datetime(df.loc[df['ACPC-1Comp_Power'] > 10, 'timestamp'])

print(count_row, count_col)
print(Timestamp1.dtypes)
Timestamp1.info()
print(Timestamp1.dt.hour.tail(6))

fig, axs = plt.subplots(2, 1)

xformatter = mdates.DateFormatter('%Y-%m-%d %H:%M')
xlocator = mdates.HourLocator(interval=120)

w, h = 2, 4
lgd = [[0 for x in range(w)] for y in range(h)]

axs[0].set_title(label='', fontsize=20)
#axs[0].set_xlabel('Time stamp')
axs[0].set_ylabel('C1DTemp')
lgd[0][0] = axs[0].plot(Timestamp1, C1DTemp,'r:', linewidth=0.5, label='Delta T')
#axs[0].set_xticklabels(Timestamp1, rotation = 20)
axs[0].xaxis.set_major_locator(xlocator)
axs[0].xaxis.set_major_formatter(xformatter)
axs[0].tick_params(axis='x', labelsize=6)
plt.setp(axs[0].get_xticklabels(), rotation=15, ha="right")
ax1 = axs[0].twinx()
ax1.set_ylabel('Flow Rate')  
lgd[0][1] = ax1.plot(Timestamp1, C1FRate, 'k--', linewidth=0.5, label='Flow Rate')
ax1.legend(handles = lgd[0][0] + lgd[0][1], loc='best')
#plt.xticks(rotation=30, ha="right")


#plt.rc('xtick',labelsize=4)
plt.title('Delta Temperature and Flow Rate with ACPC Power > 10')
plt.show()