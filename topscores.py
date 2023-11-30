import pandas as pd
import matplotlib.pyplot as plt


goalscorers = pd.read_csv('goalscorers.csv')

df = pd.DataFrame(goalscorers)

top_c = 10

name_counts = df['scorer'].value_counts()

top_countries = name_counts.head(top_c)

top_countries.plot(kind='bar')

plt.xlabel('Names')
plt.ylabel('Top goal scorers')
plt.title(f'Top {top_c} goal scorers since 1916')

#From the bar chart the top goalscorer is Christiano Ronaldo with over 100 goals followed by lewandoski

plt.show()
