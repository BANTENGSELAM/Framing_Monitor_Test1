import pandas as pd
from preprocess import clean_text
from simple_lexicon import lexicon_sentiment

def run_sentiment(input_csv='data/tweets.csv', output_csv='data/tweets_sentiment.csv'):
    df = pd.read_csv(input_csv)
    df['clean'] = df['content'].astype(str).apply(clean_text)
    df['sentiment'] = df['clean'].apply(lexicon_sentiment)
    df.to_csv(output_csv, index=False)
    print(f"✅ Hasil disimpan di {output_csv}")
    print(df['sentiment'].value_counts())

if __name__ == "__main__":
    run_sentiment()
