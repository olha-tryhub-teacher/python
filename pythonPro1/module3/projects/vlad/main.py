import pandas as pd
df = pd.read_csv("Fifa 23 Players Data.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# Топ-5 найдорожчих гравців за ринковою вартістю
top_5_valuable_players = df.nlargest(5, "Value(in Euro)")[["Full Name", "Value(in Euro)"]]
print(top_5_valuable_players)

# Топ-3 гравці з найвищим рейтингом "Overall"
top_3_overall_players = df.nlargest(3, "Overall")[["Full Name", "Overall"]]
print(top_3_overall_players)

# Кількість гравців по національностях
nationality_counts = df["Nationality"].value_counts()
print(nationality_counts)

# гравці, які грають на кількох позиціях
multi_position_players = df[df["Positions Played"].str.contains(",")][["Full Name", "Positions Played"]]
print(multi_position_players)

# Гравці зі слабкими навичками володіння м"ячем (низький "Dribbling")
weak_dribblers = df[df["Dribbling Total"] < 50][["Full Name", "Dribbling Total"]]
print(weak_dribblers)

# Гравці з найвищим рівнем фізичної підготовки ("Physicality Total")
top_physical_players = df.nlargest(5, "Physicality Total")[["Full Name", "Physicality Total"]]
print(top_physical_players)

# Порівняння середнього рівня "Shooting" та "Passing" між гравцями
average_shooting = df["Shooting Total"].mean()
average_passing = df["Passing Total"].mean()
print(f"Середній рівень стрільби: {average_shooting}, Середній рівень передач: {average_passing}")

# кількість гравців відповідно до їх віку
age_counts = df["Age"].value_counts().sort_index()
print(age_counts)
