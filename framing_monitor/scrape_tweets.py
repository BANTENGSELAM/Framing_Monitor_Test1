import snscrape.modules.twitter as sntwitter
import pandas as pd
import sys

def scrape_tweets(query, max_tweets=200, out_csv='data/tweets.csv'):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        tweets.append({
            'date': tweet.date,
            'username': tweet.user.username,
            'content': tweet.content,
            'url': f"https://twitter.com/{tweet.user.username}/status/{tweet.id}"
        })
    df = pd.DataFrame(tweets)
    df.to_csv(out_csv, index=False)
    print(f"✅ {len(df)} tweet disimpan di {out_csv}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cara pakai: python scrape_tweets.py \"kata_kunci\" [jumlah] [output_csv]")
        sys.exit(1)
    query = sys.argv[1]
    max_tweets = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    out_csv = sys.argv[3] if len(sys.argv) > 3 else 'data/tweets.csv'
    scrape_tweets(query, max_tweets, out_csv)
