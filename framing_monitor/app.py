import streamlit as st
import pandas as pd

st.title("Sistem Pemantauan Framing Negatif (Demo)")

df = pd.read_csv('data/tweets_framing.csv')

st.sidebar.header("Filter Sentimen")
sentiments = st.sidebar.multiselect("Pilih sentimen",
                                    df['sentiment'].unique(),
                                    default=df['sentiment'].unique())
filtered = df[df['sentiment'].isin(sentiments)]

st.write(f"Total tweet yang ditampilkan: {len(filtered)}")
st.dataframe(filtered[['date','username','clean','sentiment','is_framing']])

if st.button("Lihat hanya framing negatif"):
    st.dataframe(df[df['is_framing'] == True][['date','username','clean','sentiment']])
