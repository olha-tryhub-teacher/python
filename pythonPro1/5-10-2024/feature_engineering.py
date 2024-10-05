import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

# Очищення даних із першого завдання
print("👽 Очищення даних 👽")
df['Rating'].fillna(-1, inplace=True)

def set_size(size):
   if size[-1] == 'M':
      return float(size[:-1])
   elif size[-1] == 'k':
      return float(size[:-1]) / 1024
   return -1

def make_price(price):
   if price[0] == '$':
       return float(price[1:])
   return 0

def set_installs(installs):
   if installs == '0':
       return 0
   return int(installs[:-1].replace(',', ''))


df['Size'] = df['Size'].apply(set_size)
df['Price'] = df['Price'].apply(make_price)
df['Installs'] = df['Installs'].apply(set_installs)

# Заміни тип даних на дробове число (float) для цін додатків (Price)
print("👽 Зміна типу даних із int на float 👽")
print("👽 Тут він ще int 👽")
print(df["Reviews"].info())
df['Reviews'] = df['Reviews'].apply(float)
print("👽 Тут він вже float 👽")
print(df["Reviews"].info())

# Обчисли, скільки доларів розробники заробили на кожному платному додатку
print("👽 Скільки заробили 👽")
df["Profit"] = df["Installs"] * df["Price"]
print(df[df["Type"] == "Paid"][["App", "Profit", "Installs", "Price"]])
# Чому дорівнює максимальний дохід ('Profit') серед платних додатків (Type == 'Paid')?
print("👽 Максимальний заробіток 👽")
print(df[df["Type"] == "Paid"]["Profit"].max())

# Створи новий стовпець, у якому зберігатиметься кількість жанрів. Назви його 'Number of genres'

def count_genres(data):
   data = data.split(';')
   return len(data)

df["Number of genres"] = df["Genres"].apply(count_genres)

# Яка максимальна кількість жанрів (Number of genres) зберігається в датасеті?
print("👽 Максимальна кількість жанрів 👽")
print(df["Number of genres"].max())

# Бонусне завдання
# Створи новий стовпець, що зберігає сезон, в якому було зроблено останнє оновлення (Last Updated) програми. Назви його 'Season'

# Виведи на екран сезони та їх кількість у датасеті
