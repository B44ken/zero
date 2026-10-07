import pandas as pd, hashlib
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('reviews.csv')
print(f'got initial dataset with {len(df)}')

# drop empty (ie. whitespace only or literally empty) rows
df['review_text'] = df['review_text'].fillna('').astype(str).apply(lambda s: None if s.strip() == '' else s.strip())
df = df.dropna(subset=['review_text'])
print(f'dropped empty, now {len(df)}')

# dedupe on lower()ed review text
df['review_low'] = df['review_text'].apply(str.lower)
df = df.drop_duplicates(subset=['review_low'])
df = df.drop(columns=['review_low'])
print(f'dropped dupes, now {len(df)}')

df['id'] = df['review_text'].apply(lambda t: hashlib.sha256(t.encode('utf-8')).hexdigest()[:16])
df['tag'] = ''

print(df)