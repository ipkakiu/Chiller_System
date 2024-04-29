#! C:\Users\macro.ip\Desktop\Chiller_System\venv\Scripts\python.exe

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Marco ip\\OneDrive\\Desktop\\Chiller_System\\data_dump.csv") # change string to raw strong
df.head()
#plt.plot(df["timestamp"], df["CHWP-004Power_Factor"], linewidth=0.5) 

if (int(df["ACPC-1Comp_Power"])) > 10:
    C1TimeS = df["timestamp"]
    C1STemp = df["ACPC-1CHWS_Temp"] 
    C1RTemp = df["ACPC-1CHWR_Temp"]

# plot 2 subplots 
fig, ax = plt.subplots(nrows=4, ncols=1)
ax[0].plot(df["timestamp"], df["CHWS_Temp"], linewidth=0.5)
ax[1].plot(df["timestamp"], df["CHWR_Temp"], linewidth=0.5)
ax[2].plot(df["timestamp"], df["CHWP-004Power_Factor"], linewidth=0.5)
ax[3].plot(df["timestamp"], df["CHWP-004Power_Factor"], linewidth=0.5)
 

fig.suptitle('Stacked subplots in one direction')
plt.show() 
