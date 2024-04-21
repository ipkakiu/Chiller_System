#! C:\Users\macro.ip\Desktop\Chiller_System\venv\Scripts\python.exe

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\macro.ip\Desktop\Chiller_System\data_dump.csv") # change string to raw strong
df.head()
plt.plot(df["timestamp"], df["CHWP-004Power_Factor"], linewidth=0.5) 
fig, ax = plt.subplots(nrows=4, ncols=2)
ax[0].plot(x, y1)
ax[1].plot(x, y2)
 
# plot 2 subplots
ax[0].set_title('Simple plot with sin(x)')
ax[1].set_title('Simple plot with sin(x**2)')
 
fig.suptitle('Stacked subplots in one direction')
plt.show() 
