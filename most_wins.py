import pandas as pd
import matplotlib.pyplot as plt


goalscorers = pd.read_csv('goalscorers.csv')

df = pd.DataFrame(goalscorers)

top_c = 10

name_counts = df['team'].value_counts()

top_countries = name_counts.head(top_c)

top_countries.plot(kind='bar')

plt.xlabel('Countries')
plt.ylabel('No. of Wins')
plt.title(f'Top {top_c} countries with the most number of wins since 1916')

#From the plot has the most number of wins with over 1000 wins

plt.show()
