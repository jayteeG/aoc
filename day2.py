#q1
import pandas as pd
df = pd.read_csv('aoc_2.txt',sep=' ',header=None)
df.columns=['case','value']
(df[df.case=='down'].value.sum() - df[df.case=='up'].value.sum()) * df[df.case=='forward'].value.sum()
