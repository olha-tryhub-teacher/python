# --- ЧАСТИНА 2: Базові діаграми ---
import matplotlib.pyplot as plt
import seaborn as sns


# Діаграма 1: Гістограма розподілу рейтингів
plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], bins=30, kde=True, color='skyblue')
plt.title('Розподіл рейтингів додатків')
plt.xlabel('Рейтинг')
plt.ylabel('Кількість')
plt.show()

# Діаграма 2: Топ-10 категорій (Стовпчикова діаграма)
plt.figure(figsize=(12, 6))
top_categories = df['Category'].value_counts().head(10)
sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
plt.title('Топ-10 категорій за кількістю додатків')
plt.xlabel('Кількість')
plt.show()

# Діаграма 3: Безкоштовні vs Платні (Кругова діаграма)
plt.figure(figsize=(7, 7))
type_counts = df['Type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#ff9999'])
plt.title('Співвідношення типів додатків')
plt.show()
