import pandas as pd
df = pd.read_csv('california_housing_train.csv')
print(df[(df['population'] >= 0) & (df['population'] <= 500)]['median_house_value'].mean())