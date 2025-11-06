import pandas as pd
import matplotlib.pyplot as plt

def visualize(csv_file='data/tweets_framing.csv'):
    df = pd.read_csv(csv_file)

    # Pie chart sentimen
    df['sentiment'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Distribusi Sentimen')
    plt.ylabel('')
    plt.show()

    # Jumlah framing negatif
    framing_count = df['is_framing'].sum()
    print(f"Jumlah tweet dengan framing negatif: {framing_count}")

if __name__ == "__main__":
    visualize()
