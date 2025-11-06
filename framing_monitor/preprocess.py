import re
import emoji

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www.\S+', '', text)      # hapus URL
    text = re.sub(r'@\w+', '', text)                 # hapus mention
    text = re.sub(r'#', '', text)                    # hapus tanda #
    text = re.sub(r'\d+', '', text)                  # hapus angka
    text = emoji.demojize(text)                      # ubah emoji jadi teks
    text = re.sub(r'[^\w\s:]', '', text)             # hapus simbol
    text = re.sub(r'\s+', ' ', text).strip()         # hapus spasi ganda
    return text
