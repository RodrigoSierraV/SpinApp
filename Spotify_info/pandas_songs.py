import pandas as pd

df_songs = pd.read_csv('level_ytube.csv', sep=';')
df_songs = df_songs.sort_values(by='energy_level', ascending=False)

df_high = df_songs.loc[df_songs['energy_level'] >= 0.9]
df_high.to_csv('high_list.csv', index=None, header=True)

df_medium = df_songs.loc[(df_songs['energy_level'] >= 0.8) & (df_songs['energy_level'] <= 0.89)]
df_medium.to_csv('medium_list.csv', index=None, header=True)


df_low = df_songs.loc[(df_songs['energy_level'] >= 0.7) & (df_songs['energy_level'] <= 0.79)]
df_low.to_csv('low_list.csv', index=None, header=True)

print(df_high, df_medium, df_low)

