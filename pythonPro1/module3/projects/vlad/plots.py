import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df = pd.read_csv("Fifa 23 Players Data.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# Топ-5 найдорожчих гравців за ринковою вартістю
top_5_valuable_players = df.nlargest(5, "Value(in Euro)")[["Full Name", "Value(in Euro)"]]
print(top_5_valuable_players)

# Графік: Топ-5 найдорожчих гравців
plt.figure(figsize=(10, 6))
plt.barh(top_5_valuable_players["Full Name"], top_5_valuable_players["Value(in Euro)"], color='gold')
plt.title('Топ-5 найдорожчих гравців за ринковою вартістю')
plt.xlabel('Вартість (в Євро)')
plt.ylabel('Гравці')
plt.grid(axis='x')
plt.show()

# Топ-3 гравці з найвищим рейтингом "Overall"
top_3_overall_players = df.nlargest(3, "Overall")[["Full Name", "Overall"]]
print(top_3_overall_players)

# Графік: Топ-3 гравці з найвищим рейтингом
plt.figure(figsize=(10, 6))
plt.bar(top_3_overall_players["Full Name"], top_3_overall_players["Overall"], color='lightblue')
plt.title('Топ-3 гравці з найвищим рейтингом "Overall"')
plt.ylabel('Рейтинг')
plt.xlabel('Гравці')
plt.xticks(rotation=15)
plt.grid(axis='y')
plt.show()

# Кількість гравців по національностях (топ 10)
nationality_counts = df["Nationality"].value_counts().head(10)
print(nationality_counts)

# Графік: Кількість гравців по національностях
plt.figure(figsize=(12, 8))
nationality_counts.plot(kind='bar', color='green')
plt.title('Кількість гравців по національностях, топ 10')
plt.xlabel('Національність')
plt.ylabel('Кількість гравців')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Гравці, які грають на кількох позиціях
multi_position_players = df[df["Positions Played"].str.contains(",")][["Full Name", "Positions Played"]]
print(multi_position_players)

# Гравці з найвищим рівнем фізичної підготовки ("Physicality Total")
top_physical_players = df.nlargest(5, "Physicality Total")[["Full Name", "Physicality Total"]]
print(top_physical_players)

# Графік: Топ-5 гравців з найвищим рівнем фізичної підготовки
plt.figure(figsize=(10, 6))
plt.barh(top_physical_players["Full Name"], top_physical_players["Physicality Total"], color='purple')
plt.title('Топ-5 гравців з найвищим рівнем фізичної підготовки')
plt.xlabel('Фізична підготовка')
plt.ylabel('Гравці')
plt.grid(axis='x')
plt.show()

# Порівняння середнього рівня "Shooting" та "Passing" між гравцями
average_shooting = df["Shooting Total"].mean()
average_passing = df["Passing Total"].mean()
print(f"Середній рівень стрільби: {average_shooting}, Середній рівень передач: {average_passing}")

# Графік: Порівняння середнього рівня "Shooting" та "Passing"
plt.figure(figsize=(8, 6))
plt.bar(['Shooting', 'Passing'], [average_shooting, average_passing], color=['orange', 'blue'])
plt.title('Середній рівень "Shooting" та "Passing"')
plt.ylabel('Середній рівень')
plt.grid(axis='y')
plt.show()

# Кількість гравців відповідно до їх віку
age_counts = df["Age"].value_counts().sort_index()
print(age_counts)

# Графік: Кількість гравців відповідно до їх віку
plt.figure(figsize=(12, 6))
age_counts.plot(kind='bar', color='cyan')
plt.title('Кількість гравців за віком')
plt.xlabel('Вік')
plt.ylabel('Кількість гравців')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()
