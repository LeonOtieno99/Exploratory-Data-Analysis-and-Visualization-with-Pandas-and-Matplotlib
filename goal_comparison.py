import pandas as pd
import matplotlib.pyplot as plt

goalscorers = pd.read_csv('goalscorers.csv', index_col=0, parse_dates=True)

goalscorers.plot()
#based on the data there has been an increased number of goals between 1956 and 2023 than from 1916 to 1955

plt.show()