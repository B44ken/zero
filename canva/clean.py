import pandas as pd

limit = 10

df = pd.read_csv('reviews.csv')
print(f'got initial dataset with {len(df)}')

df = df.dropna()
print(f'dropped empty, now {len(df)}')

df = df.drop_duplicates(subset=['review_text'])
print(f'dropped dupes, now {len(df)}')

print('')
for s in df.to_dict(orient='records')[0:limit]:
  print(f'{s['review_title']}:\n{s['review_text']}\n')