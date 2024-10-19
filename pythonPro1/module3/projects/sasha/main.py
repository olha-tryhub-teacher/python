import pandas as pd
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