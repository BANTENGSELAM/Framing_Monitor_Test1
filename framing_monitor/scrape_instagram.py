# scrape_instagram.py
import instaloader
import pandas as pd
import sys
from datetime import datetime

L = instaloader.Instaloader(download_comments=False, save_metadata=False, post_metadata_txt_pattern="")

def scrape_hashtag(hashtag, max_posts=100, out_csv="data/instagram.csv"):
    posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()
    data = []
    count = 0
    for post in posts:
        if count >= max_posts:
            break
        caption = post.caption or ""
        data.append({
            "platform":"instagram",
            "source": post.owner_username,
            "id": post.shortcode,
            "date": post.date_utc.isoformat(),
            "text": caption,
            "link": f"https://www.instagram.com/p/{post.shortcode}/",
            "raw": ""
        })
        count += 1
    df = pd.DataFrame(data)
    df.to_csv(out_csv, index=False, encoding="utf-8-sig")
    print(f"✅ {len(df)} Instagram posts (#{hashtag}) disimpan ke {out_csv}")

if __name__ == "__main__":
    tag = sys.argv[1] if len(sys.argv) > 1 else "mahasiswa"
    m = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    scrape_hashtag(tag, m)
