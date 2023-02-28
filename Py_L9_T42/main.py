import pandas as pd
df = pd.read_csv('california_housing_train.csv')
print(df[df['population'] == df['population'].min()]['households'].max())