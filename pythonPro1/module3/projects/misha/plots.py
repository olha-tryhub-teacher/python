import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gym_members_exercise_tracking.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# 1. Вплив типу тренування на спалювання калорій
calories_by_workout = df.groupby('Workout_Type')['Calories_Burned'].mean().reset_index()

# 2. Середнє спалення калорій за тривалістю тренування
avg_calories_duration = df.groupby('Session_Duration (hours)')['Calories_Burned'].mean().reset_index()

# 3. Вплив статі на спалювання калорій
calories_by_gender = df.groupby('Gender')['Calories_Burned'].mean().reset_index()

# 4. Вплив віку на спалювання калорій
age_calories = df[['Age', 'Calories_Burned']].groupby('Age').mean().reset_index()

# 5. Залежність між частотою тренувань та спалюванням калорій
calories_workout_freq = df.groupby('Workout_Frequency (days/week)')['Calories_Burned'].mean().reset_index()

# 6. Взаємозв’язок між досвідом та частотою тренувань
experience_freq = df.groupby('Experience_Level')['Workout_Frequency (days/week)'].mean().reset_index()

# Візуалізація результатів

# 1. Вплив типу тренування на спалювання калорій
plt.figure(figsize=(10, 5))
plt.bar(calories_by_workout['Workout_Type'], calories_by_workout['Calories_Burned'], color='skyblue')
plt.title('Середнє спалювання калорій за типом тренування')
plt.xlabel('Тип тренування')
plt.ylabel('Середнє спалювання калорій')
plt.xticks(rotation=45)
plt.show()

# 3. Вплив статі на спалювання калорій
plt.figure(figsize=(6, 4))
plt.bar(calories_by_gender['Gender'], calories_by_gender['Calories_Burned'], color='salmon')
plt.title('Середнє спалювання калорій за статтю')
plt.xlabel('Стать')
plt.ylabel('Середнє спалювання калорій')
plt.xticks(rotation=0)
plt.show()

# 4. Вплив віку на спалювання калорій
plt.figure(figsize=(10, 5))
plt.plot(age_calories['Age'], age_calories['Calories_Burned'], marker='o')
plt.title('Середнє спалювання калорій за віком')
plt.xlabel('Вік')
plt.ylabel('Середнє спалювання калорій')
plt.grid()
plt.show()

# 5. Залежність між частотою тренувань та спалюванням калорій
plt.figure(figsize=(10, 5))
plt.bar(calories_workout_freq['Workout_Frequency (days/week)'], calories_workout_freq['Calories_Burned'], color='lightgreen')
plt.title('Середнє спалювання калорій за частотою тренувань')
plt.xlabel('Частота тренувань (дні/тиждень)')
plt.ylabel('Середнє спалювання калорій')
plt.xticks(rotation=0)
plt.show()
