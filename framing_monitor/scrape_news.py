import feedparser
import pandas as pd
from datetime import datetime

# --- Kata kunci pencarian ---
keyword = "Intoleran"

# --- Daftar sumber berita (RSS feed populer di Indonesia) ---
rss_feeds = {
    "Kompas": f"https://news.google.com/rss/search?q={keyword}+site:kompas.com&hl=id&gl=ID&ceid=ID:id",
    "Detik": f"https://news.google.com/rss/search?q={keyword}+site:detik.com&hl=id&gl=ID&ceid=ID:id",
    "CNN Indonesia": f"https://news.google.com/rss/search?q={keyword}+site:cnnindonesia.com&hl=id&gl=ID&ceid=ID:id",
    "Tempo": f"https://news.google.com/rss/search?q={keyword}+site:tempo.co&hl=id&gl=ID&ceid=ID:id"
}

# --- Simpan hasil ---
articles = []

for source, url in rss_feeds.items():
    print(f"Mengambil berita dari {source}...")
    feed = feedparser.parse(url)
    for entry in feed.entries:
        articles.append({
            "sumber": source,
            "judul": entry.title,
            "link": entry.link,
            "tanggal": entry.published if "published" in entry else datetime.now().isoformat(),
            "ringkasan": entry.summary if "summary" in entry else ""
        })

# --- Simpan ke CSV ---
df = pd.DataFrame(articles)
df.to_csv("data/news.csv", index=False, encoding="utf-8-sig")
print(f"✅ {len(df)} berita tentang '{keyword}' disimpan ke data/news.csv")
