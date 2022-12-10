import pandas as pd

data = pd.read_csv('C:/Users/PC/Documents/prak12 algo/Negara2.csv')

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print('Berikut Data Framenya:')
print(df, '\n')

print('Berikut Data Mean:')
print(mean, '\n')

print('Berikut Data Standar Deviasi:')
print(std, '\n')

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandarDeviasi.csv')
print('File Berhasil Dibuat')