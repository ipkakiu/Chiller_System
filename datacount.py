#! C:\Users\macro.ip\Desktop\Chiller_System\venv\Scripts\python.exe

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\macro.ip\Desktop\Chiller_System\data_dump.csv") # change string to raw strong


count_row = df.shape[0]  # Gives number of rows
count_col = df.shape[1]  # Gives number of columns
print(count_row, count_col)