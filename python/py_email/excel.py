import pandas as pd
df = pd.read_excel('Testdata1.xlsx')
# filtered_df = df[df['roll'] == 3]
condition1 = df['Tower'] == 'IoT'
condition2 = df['Roll Off Status'] == 'BENCH'
filtered_df = df[condition1 & condition2]
print(filtered_df.head(10))
filtered_df.to_excel('Testdata2.xlsx', index=False)
