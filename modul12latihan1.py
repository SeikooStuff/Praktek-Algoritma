import pandas as pd

data = pd.read_csv('C:/Users/PC/Documents/prak12 algo/Negara2.csv')

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print(df)
print(mean)
print(std)