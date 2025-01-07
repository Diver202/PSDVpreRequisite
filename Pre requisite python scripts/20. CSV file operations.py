import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Jupyter notebook/data.csv')
column= 'Numbers'  
column_sum = data[column].sum()
print(f"Sum : {column_sum}")
    
plt.plot(data[column], marker='o', linestyle='--')

plt.xlabel('Index')
plt.ylabel(column)
plt.grid(True)
plt.show()