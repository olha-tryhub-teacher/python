import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# Найгірша та найкраща якість сну за професією
worst_sleep_by_occupation = df.groupby("Occupation")["Quality of Sleep"].min()
best_sleep_by_occupation = df.groupby("Occupation")["Quality of Sleep"].max()

plt.figure(figsize=(12, 6))
plt.bar(worst_sleep_by_occupation.index, worst_sleep_by_occupation.values, color="red", label="Найгірша якість сну")
plt.bar(best_sleep_by_occupation.index, best_sleep_by_occupation.values, color="green", alpha=0.7, label="Найкраща якість сну")
plt.xticks(rotation=90)
plt.title("Якість сну за професією")
plt.xlabel("Професія")
plt.ylabel("Якість сну")
plt.legend()
plt.show()

# Найгірша та найкраща якість сну за віком
worst_sleep_by_age = df.groupby("Age")["Quality of Sleep"].min()
best_sleep_by_age = df.groupby("Age")["Quality of Sleep"].max()

plt.figure(figsize=(12, 6))
plt.plot(worst_sleep_by_age.index, worst_sleep_by_age.values, marker='o', color="red", label="Найгірша якість сну")
plt.plot(best_sleep_by_age.index, best_sleep_by_age.values, marker='o', color="green", label="Найкраща якість сну")
plt.title("Якість сну за віком")
plt.xlabel("Вік")
plt.ylabel("Якість сну")
plt.legend()
plt.show()

# Найгірша та найкраща якість сну за статтю
worst_sleep_by_gender = df.groupby("Gender")["Quality of Sleep"].min()
best_sleep_by_gender = df.groupby("Gender")["Quality of Sleep"].max()

plt.figure(figsize=(6, 4))
plt.bar(["Чоловіки", "Жінки"], worst_sleep_by_gender, color="red", label="Найгірша якість сну")
plt.bar(["Чоловіки", "Жінки"], best_sleep_by_gender, color="green", alpha=0.7, label="Найкраща якість сну")
plt.title("Якість сну за статтю")
plt.xlabel("Стать")
plt.ylabel("Якість сну")
plt.legend()
plt.show()

# Кореляція між рівнем фізичної активності та якістю сну
activity_sleep_correlation = df["Physical Activity Level"].corr(df["Quality of Sleep"])
print(f"Кореляція між рівнем фізичної активності та якістю сну: {activity_sleep_correlation:.2f}")

# Середня якість сну за категорією BMI
bmi_sleep_relationship = df.groupby("BMI Category")["Quality of Sleep"].mean()

plt.figure(figsize=(8, 5))
plt.bar(bmi_sleep_relationship.index, bmi_sleep_relationship.values, color="skyblue")
plt.title("Середня якість сну за категорією BMI")
plt.xlabel("Категорія BMI")
plt.ylabel("Середня якість сну")
plt.xticks(rotation=45)
plt.show()

# Середня тривалість сну за віком
avg_sleep_duration_by_age = df.groupby("Age")["Sleep Duration"].mean()

plt.figure(figsize=(12, 6))
plt.plot(avg_sleep_duration_by_age.index, avg_sleep_duration_by_age.values, marker='o', color="blue", label="Середня тривалість сну")
plt.title("Середня тривалість сну за віком")
plt.xlabel("Вік")
plt.ylabel("Тривалість сну")
plt.legend()
plt.show()

# Середня якість сну за віком
avg_quality_of_sleep_by_age = df.groupby("Age")["Quality of Sleep"].mean()

plt.figure(figsize=(12, 6))
plt.plot(avg_quality_of_sleep_by_age.index, avg_quality_of_sleep_by_age.values, marker='o', color="purple", label="Середня якість сну")
plt.title("Середня якість сну за віком")
plt.xlabel("Вік")
plt.ylabel("Якість сну")
plt.legend()
plt.show()
