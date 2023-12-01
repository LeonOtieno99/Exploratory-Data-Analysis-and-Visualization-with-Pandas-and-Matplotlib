import pandas as pd
import matplotlib.pyplot as plt


tournaments = pd.read_csv('results.csv')

df = pd.DataFrame(tournaments)

top_t = 10

name_counts = df['tournament'].value_counts()

top_countries = name_counts.head(top_t)

top_countries.plot(kind='bar')

plt.xlabel('tournaments')
plt.ylabel('games played')
plt.title(f'Top {top_t} goal scorers since 1916')

#From the bar chart the most played tournament is the friendlies followed by fifa qualifiers game

plt.show()
