import pandas as pd
import matplotlib.pyplot as plt

# Завантаження датасету
df = pd.read_csv("Medical_Appointment_No_Shows.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# 1. Вплив віку на ймовірність неявки
age_no_show = df.groupby("Age")["No-show"].value_counts(normalize=True).unstack()
print("Вплив віку на ймовірність неявки:\n", age_no_show)

# 2. Різниця в неявках за статтю
gender_no_show = df.groupby("Gender")["No-show"].value_counts(normalize=True).unstack()
print("\nНеявки за статтю:\n", gender_no_show)

# 3. Вплив хронічних захворювань на неявки
chronic_conditions = ["Hipertension", "Diabetes", "Alcoholism", "Handcap"]
for condition in chronic_conditions:
    condition_no_show = df.groupby(condition)["No-show"].value_counts(normalize=True).unstack()
    print(f"\nВплив {condition} на ймовірність неявки:\n", condition_no_show)

# 4. Вплив SMS-нагадувань на неявки
sms_no_show = df.groupby("SMS_received")["No-show"].value_counts(normalize=True).unstack()
print("\nВплив SMS-нагадувань на ймовірність неявки:\n", sms_no_show)

# 5. Аналіз сусідства
neighbourhood_no_show = df.groupby("Neighbourhood")["No-show"].value_counts(normalize=True).unstack()
# Вибірка лише найбільш частих районів для кращої візуалізації
top_neighbourhoods = neighbourhood_no_show.sum(axis=1).nlargest(10).index
print("\nНеявки за найбільш поширеними районами:\n", neighbourhood_no_show.loc[top_neighbourhoods])

# Візуалізація

# 1. Вплив віку на ймовірність неявки
plt.figure(figsize=(10, 6))
age_no_show.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'])
plt.title('Вплив віку на ймовірність неявки')
plt.xlabel('Вік')
plt.ylabel('Ймовірність неявки')
plt.xticks(rotation=45)
plt.legend(title='Неявка', labels=['Так', 'Ні'])
plt.grid(axis='y')
plt.show()

# 2. Неявки за статтю
plt.figure(figsize=(10, 6))
gender_no_show.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'])
plt.title('Неявки за статтю')
plt.xlabel('Стать')
plt.ylabel('Ймовірність неявки')
plt.xticks(rotation=0)
plt.legend(title='Неявка', labels=['Так', 'Ні'])
plt.grid(axis='y')
plt.show()

# 3. Вплив хронічних захворювань на ймовірність неявки
for condition in chronic_conditions:
    plt.figure(figsize=(10, 6))
    condition_no_show = df.groupby(condition)["No-show"].value_counts(normalize=True).unstack()
    condition_no_show.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'])
    plt.title(f'Вплив {condition} на ймовірність неявки')
    plt.xlabel(condition)
    plt.ylabel('Ймовірність неявки')
    plt.xticks(rotation=0)
    plt.legend(title='Неявка', labels=['Так', 'Ні'])
    plt.grid(axis='y')
    plt.show()

# 4. Вплив SMS-нагадувань на неявки
plt.figure(figsize=(10, 6))
sms_no_show.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'])
plt.title('Вплив SMS-нагадувань на ймовірність неявки')
plt.xlabel('SMS-нагадування')
plt.ylabel('Ймовірність неявки')
plt.xticks(rotation=0)
plt.legend(title='Неявка', labels=['Так', 'Ні'])
plt.grid(axis='y')
plt.show()

# 5. Неявки за найбільш поширеними районами
plt.figure(figsize=(12, 6))
neighbourhood_no_show.loc[top_neighbourhoods].plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'])
plt.title('Неявки за найбільш поширеними районами')
plt.xlabel('Район')
plt.ylabel('Ймовірність неявки')
plt.xticks(rotation=45)
plt.legend(title='Неявка', labels=['Так', 'Ні'])
plt.grid(axis='y')
plt.show()
