neg_words = {
    "buruk","jahat","berbahaya","mengancam","bodoh","meresahkan",
    "penjahat","kejam","melanggar","rusak","menakutkan","kotor"
}

pos_words = {
    "bagus","aman","baik","membantu","positif","solusi","terpercaya","indah"
}

def lexicon_sentiment(text):
    words = text.split()
    neg_score = sum(1 for w in words if w in neg_words)
    pos_score = sum(1 for w in words if w in pos_words)
    if neg_score > pos_score:
        return "negative"
    elif pos_score > neg_score:
        return "positive"
    else:
        return "neutral"
