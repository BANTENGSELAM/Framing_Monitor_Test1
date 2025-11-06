import pandas as pd

def detect_negative_framing(input_csv='data/tweets_sentiment.csv',
                            output_csv='data/tweets_framing.csv',
                            keywords=None):
    if keywords is None:
        keywords = ["kelompok x"]  # ubah sesuai topik kamu

    df = pd.read_csv(input_csv)
    df['is_framing'] = df.apply(
        lambda row: any(k.lower() in row['clean'] for k in keywords)
        and row['sentiment'] == 'negative', axis=1)
    df.to_csv(output_csv, index=False)
    print(f"✅ Deteksi framing selesai, disimpan di {output_csv}")
    print(df['is_framing'].value_counts())

if __name__ == "__main__":
    detect_negative_framing()
