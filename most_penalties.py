import pandas as pd
import matplotlib.pyplot as plt


goalscorers = pd.read_csv('goalscorers.csv')

df = pd.DataFrame(goalscorers)

#penalty for each match
df['TotalPenalties'] = df['penalty'].fillna(False).astype(int)


matches_penalties = df.groupby(['home_team', 'away_team'])['TotalPenalties'].sum().reset_index()

sorted_matches = matches_penalties.sort_values(by='TotalPenalties', ascending=False)

top_matches = sorted_matches.head(10)
print(top_matches)

top_matches.plot(kind='bar', xlabel=['home_team','away_team'], ylabel='TotalPenalties')
plt.title('Matches with the most penalties')

#check output from cmd and compare numbers
#game with highest number of penalties is argentina and paraguay with 11 shown as 215

plt.show()

