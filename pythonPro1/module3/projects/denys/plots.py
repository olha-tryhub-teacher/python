import pandas as pd
import matplotlib.pyplot as plt

full_df = pd.read_csv("steam.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# Графік кількості додатків за жанрами
genres_split = full_df["genres"].str.split(";", expand=True)
all_genres = genres_split.stack()
genres_counts = all_genres.value_counts()
plt.figure(figsize=(10, 6))
plt.bar(genres_counts.index, genres_counts.values, color="skyblue")
plt.xticks(rotation=90)
plt.title("Кількість додатків за жанрами")
plt.xlabel("Жанр")
plt.ylabel("Кількість")
plt.show()

# Графік розсіювання середнього часу гри по жанрах
full_df["genres_split"] = full_df["genres"].str.split(";")
df_genres = full_df.explode("genres_split")
average_playtime_by_genre = df_genres.groupby("genres_split")[["average_playtime", "price"]].mean()

plt.figure(figsize=(10, 6))
plt.scatter(average_playtime_by_genre["price"], average_playtime_by_genre["average_playtime"], color="purple")
for genre, row in average_playtime_by_genre.iterrows():
    plt.text(row["price"], row["average_playtime"], genre, fontsize=8, ha="right")
plt.xlabel("Ціна")
plt.ylabel("Середній час гри")
plt.title("Залежність середнього часу гри від ціни по жанрах")
plt.grid(True)
plt.show()

# Кругова діаграма для кількості додатків по платформах
app_per_platform = full_df.groupby(by="platforms")["name"].count().sort_values(ascending=False)
plt.figure(figsize=(8, 8))
plt.pie(app_per_platform, labels=app_per_platform.index, autopct='%1.1f%%', startangle=140, colors=["#ff9999","#66b3ff","#99ff99","#ffcc99"])
plt.title("Кількість додатків по платформах")
plt.show()

# Лінійний графік для кількості інді ігор за кожний рік
df = full_df[full_df["genres"].str.contains("Indie")]
df["release_date"] = pd.to_datetime(df["release_date"])
df["year"] = df["release_date"].dt.year
df_filtered = df[df["year"] <= 2018]
count_per_year = df_filtered.groupby("year")["name"].count()

plt.figure(figsize=(10, 6))
plt.plot(count_per_year.index, count_per_year.values, marker='o', color='blue', linestyle='--')
plt.xlabel("Рік")
plt.ylabel("Кількість інді ігор")
plt.title("Кількість інді ігор за кожний рік")
plt.grid(True)
plt.show()
