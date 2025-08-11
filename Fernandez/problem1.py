import pandas
import os
# read the CSV file and find out how many medals the US won in the olympics
olympics_file = r"C:/Users/Ray/Documents/GitHub/Class/AI2C-Prereqs/lesson09/Pandas/all_olympic_medalists.csv"
df = pandas.read_csv(olympics_file)

#clear NaN/NA values
df = df[df['country_code'].notna()]
#filter for USA
df = df[df['country_code'].str.contains('USA')]
print(len(df.index))
