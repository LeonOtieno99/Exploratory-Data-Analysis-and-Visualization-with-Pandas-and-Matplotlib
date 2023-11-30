import pandas as pd
import matplotlib.pyplot as plt


goalscorers = pd.read_csv('goalscorers.csv')

df = pd.DataFrame(goalscorers)

top_c = 10

name_counts = df['minute'].value_counts()

top_countries = name_counts.head(top_c)

top_countries.plot(kind='bar')

plt.xlabel('minute')
plt.ylabel('No. of goals')
plt.title('Minute with most number of goals')

#Quite shocking the 90th minute has the most number of goals

plt.show()
