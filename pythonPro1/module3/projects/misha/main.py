import pandas as pd
df = pd.read_csv("gym_members_exercise_tracking.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# 1. Вплив типу тренування на спалювання калорій
calories_by_workout = df.groupby('Workout_Type')['Calories_Burned'].mean().reset_index()
print("Середнє спалювання калорій за типом тренування:\n", calories_by_workout)

# 2. Середнє спалення калорій за тривалістю тренування
avg_calories_duration = df.groupby('Session_Duration (hours)')['Calories_Burned'].mean().reset_index()
print(f"Середнє спалення калорій за тривалістю тренування:\n", avg_calories_duration)

# 3. Вплив статі на спалювання калорій
calories_by_gender = df.groupby('Gender')['Calories_Burned'].mean().reset_index()
print("Середнє спалювання калорій за статтю:\n", calories_by_gender)

# 4. Вплив віку на спалювання калорій
age_calories = df[['Age', 'Calories_Burned']].groupby('Age').mean().reset_index()
print("Середнє спалювання калорій за віком:\n", age_calories)

# 5. Залежність між частотою тренувань та спалюванням калорій
calories_workout_freq = df.groupby('Workout_Frequency (days/week)')['Calories_Burned'].mean().reset_index()  # Середнє спалення калорій за частотою тренувань
print("\nСереднє спалення калорій за частотою тренувань:\n", calories_workout_freq)

# 6. Взаємозв’язок між досвідом та частотою тренувань
experience_freq = df.groupby('Experience_Level')['Workout_Frequency (days/week)'].mean().reset_index()  # Середня частота тренувань за рівнем досвіду
print("\nСередня частота тренувань за рівнем досвіду:\n", experience_freq)