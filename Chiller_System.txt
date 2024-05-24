#! C:\Users\macro.ip\Desktop\Chiller_System\venv\Scripts\python.exe

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

df = pd.read_csv("C:\\Users\\Marco ip\\OneDrive\\Desktop\\Chiller_System\\data_dump.csv") # change string to raw strong
#plt.plot(df["timestamp"], df["CHWP-004Power_Factor"], linewidth=0.5) 

#df['ACPC-1Comp_Power'] = df['ACPC-1Comp_Power'].apply(lambda x: x['timestamp'])
#ACPC1Comp_Power = list(filter(lambda x: x>10,df['ACPC-1Comp_Power']))
C1STemp = df.loc[df['ACPC-1Comp_Power'] > 10, 'ACPC-1CHWS_Temp']
C1RTemp = df.loc[df['ACPC-1Comp_Power'] > 10, 'ACPC-1CHWR_Temp']
C1FRate = df.loc[df['ACPC-1Comp_Power'] > 10, 'ACPC-1Flow_Rate']
C1DTemp = C1STemp - C1RTemp
Timestamp1 = pd.to_datetime(df.loc[df['ACPC-1Comp_Power'] > 10, 'timestamp'])
#ACPC2Comp_Power = list(filter(lambda x: x>10,df['ACPC-1Comp_Power']))
C2STemp = df.loc[df['ACPC-2Comp_Power'] > 10, 'ACPC-2CHWS_Temp']
C2RTemp = df.loc[df['ACPC-2Comp_Power'] > 10, 'ACPC-2CHWR_Temp']
C2FRate = df.loc[df['ACPC-2Comp_Power'] > 10, 'ACPC-2Flow_Rate']
C2DTemp = C2STemp - C2RTemp
Timestamp2 = pd.to_datetime(df.loc[df['ACPC-2Comp_Power'] > 10, 'timestamp'])
#ACPC3Comp_Power = list(filter(lambda x: x>10,df['ACPC-1Comp_Power']))
Timestamp3 = df.loc[df['ACPC-3Comp_Power'] > 10, 'timestamp']
C3STemp = df.loc[df['ACPC-3Comp_Power'] > 10, 'ACPC-3CHWS_Temp']
C3RTemp = df.loc[df['ACPC-3Comp_Power'] > 10, 'ACPC-3CHWR_Temp']
C3FRate = df.loc[df['ACPC-3Comp_Power'] > 10, 'ACPC-3Flow_Rate']
C3DTemp = C3STemp - C3RTemp
Timestamp3 = pd.to_datetime(df.loc[df['ACPC-3Comp_Power'] > 10, 'timestamp'])
#ACPC4Comp_Power = list(filter(lambda x: x>10,df['ACPC-1Comp_Power']))
Timestamp4 = df.loc[df['ACPC-4Comp_Power'] > 10, 'timestamp']
C4STemp = df.loc[df['ACPC-4Comp_Power'] > 10, 'ACPC-4CHWS_Temp']
C4RTemp = df.loc[df['ACPC-4Comp_Power'] > 10, 'ACPC-4CHWR_Temp']
C4FRate = df.loc[df['ACPC-4Comp_Power'] > 10, 'ACPC-4Flow_Rate']
C4DTemp = C4STemp - C4RTemp
Timestamp4 = pd.to_datetime(df.loc[df['ACPC-4Comp_Power'] > 10, 'timestamp'])

# if (int(df["ACPC-1Comp_Power"])) > 10:
#     C1TimeS = df["timestamp"]
#     C1STemp = df["ACPC-1CHWS_Temp"] 
#     C1RTemp = df["ACPC-1CHWR_Temp"]

#Format ticklabels at specificed locations (set_xtickslabels will removes DateFormattor and replaced with a Fixed Formatter)
#Never use set_xticklabels without specifying a custom locator, e.g. via set_xticks
xformatter = mdates.DateFormatter('%Y-%m-%d %H:%M')
xlocator = mdates.HourLocator(interval=120)

#create 4x1 subplots    
fig, axs = plt.subplots(4, 1, figsize=(5, 200), tight_layout=True, sharex=True, clear=True)
#fig.subplots_adjust(wspace=1, hspace=0.4)
#list for legend labels
w, h = 2, 4
lgd = [[0 for x in range(w)] for y in range(h)]


# plot 2 subplots 
#plt.subplot(4,1,1)
axs[0].set_title(label='ACPC1', fontsize=10)
#axs[0].set_xlabel('Time stamp')
axs[0].set_ylabel('Delta Temp')
lgd[0][0] = axs[0].plot(Timestamp1, C1DTemp,'r:', linewidth=0.5, label='Delta T')
axs[0].xaxis.set_major_locator(xlocator)
axs[0].xaxis.set_major_formatter(xformatter)
axs[0].tick_params(axis='x', labelsize=6)
#axs[0].set_xticklabels(axs[0].get_xticks(), rotation = 50)
plt.setp(axs[0].get_xticklabels(), rotation=15, ha="center")
ax0 = axs[0].twinx()
ax0.set_ylabel('Flow Rate')  
lgd[0][1] = ax0.plot(Timestamp1, C1FRate, 'k--', linewidth=0.5, label='Flow Rate')
ax0.legend(handles = lgd[0][0] + lgd[0][1], loc='lower right')

#plt.subplot(4,1,2)
#axs[1].set_xlabel('Time stamp')
#axs[1].set_xticklabels(axs[1].get_xticks(), rotation = 50)
axs[1].set_title(label='ACPC2', fontsize=10)
axs[1].set_ylabel('Delta Temp')
lgd[1][0] = axs[1].plot(Timestamp2, C2DTemp,'g:', linewidth=0.5, label='Delta T')
axs[1].xaxis.set_major_locator(xlocator)
axs[1].xaxis.set_major_formatter(xformatter)
axs[1].tick_params(axis='x', labelsize=6)
plt.setp(axs[1].get_xticklabels(), rotation=15, ha="center")
ax1 = axs[1].twinx()
ax1.set_ylabel('Flow Rate')  
lgd[1][1] = ax1.plot(Timestamp2, C2FRate, 'k--', linewidth=0.5, label='Flow Rate')
ax1.legend(handles = lgd[1][0] + lgd[1][1], loc='lower right')

#plt.subplot(4,1,3)
#axs[2].set_xlabel('Time stamp')
#axs[2].set_xticklabels(axs[2].get_xticks(), rotation = 50)
#plt.xticks(np.arange(0, len(Timestamp3), 96), rotation=30)
axs[2].set_title(label='ACPC3', fontsize=10)
axs[2].set_ylabel('Delta Temp')
lgd[2][0] = axs[2].plot(Timestamp3, C3DTemp,'b:', linewidth=0.5, label='Delta T')
axs[2].xaxis.set_major_locator(xlocator)
axs[2].xaxis.set_major_formatter(xformatter)
axs[2].tick_params(axis='x', labelsize=6)
plt.setp(axs[2].get_xticklabels(), rotation=15, ha="center")
ax2 = axs[2].twinx()
ax2.set_ylabel('Flow Rate')  
lgd[2][1] = ax2.plot(Timestamp3, C3FRate, 'k--', linewidth=0.5, label='Flow Rate')
ax2.legend(handles = lgd[2][0] + lgd[2][1], loc='lower right')

#plt.subplot(4,1,4)
#axs[3].set_xlabel('Time stamp')
#axs[3].set_xticklabels(axs[3].get_xticks(), rotation = 50)
#plt.xticks(np.arange(0, len(Timestamp4), 96), rotation=30)
axs[3].set_title(label='ACPC4', fontsize=10)
axs[3].set_ylabel('Delta Temp')
lgd[3][0] = axs[3].plot(Timestamp4, C4DTemp,'y:', linewidth=0.5, label='Delta T')
axs[3].xaxis.set_major_locator(xlocator)
axs[3].xaxis.set_major_formatter(xformatter)
axs[3].tick_params(axis='x', labelsize=6)
plt.setp(axs[3].get_xticklabels(), rotation=15, ha="center")
ax3 = axs[3].twinx()
ax3.set_ylabel('Flow Rate')  
lgd[3][1] = ax3.plot(Timestamp4, C4FRate, 'k--', linewidth=0.5, label='Flow Rate')
ax3.legend(handles = lgd[3][0] + lgd[3][1], loc='lower right')

#[t.set_visible(True) for t in ax.get_xticklabels()]
#axs.xaxis.set_major_locator(xlocator)
#plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
fig.suptitle('Delta Temperature and Flow Rate with ACPC Power > 10')
plt.show()
#plt.savefig('Chiller System Observation')
