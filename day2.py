import pandas as pd
#q1

df = pd.read_csv('aoc_2.txt',sep=' ',header=None, names=['case','value'])
q1 = (df[df.case=='down'].value.sum() - df[df.case=='up'].value.sum()) * df[df.case=='forward'].value.sum()

#q2

def calculate_aim(row):
    if row['case']=='forward':
        return 0 
    elif row['case']=='down':
        return row['value']
    elif row['case']=='up':
        return -1*row['value']
      
df['depth'] = df['value'] * df.apply(calculate_aim,axis=1).cumsum()
q2 = df[df.case=='forward'].depth.sum() * df[df.case=='forward'].value.sum()

print(f"q1: {q1}")
print(f"q2: {q2}")
