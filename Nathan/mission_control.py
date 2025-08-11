import pandas as pd
import numpy as np

datafile = pd.read_csv('all_olympic_medalists.csv', usecols=['country'])

total_usa = datafile[datafile['country'] == 'United States'].count()

print(f'Total USA medals: {total_usa}')
