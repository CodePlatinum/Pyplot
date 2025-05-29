import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("movies_dataset.csv")

# Обробка бюджету та країн
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['main_country'] = df['countries_origin'].apply(lambda x: eval(x)[0] if pd.notnull(x) and len(eval(x)) > 0 else None)

# Групування та побудова
avg_budget = df.groupby('main_country')['budget'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
avg_budget.plot(kind='bar', color='skyblue')
plt.title("Середній бюджет фільмів за країнами (топ-10)")
plt.ylabel("Середній бюджет (USD)")
plt.xticks(rotation=45)
plt.show()



 #--------

df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['grossWorldWide'] = pd.to_numeric(df['grossWorldWide'], errors='coerce')

yearly_gross = df.groupby('Year')['grossWorldWide'].sum().dropna()

plt.figure(figsize=(12, 6))
plt.plot(yearly_gross.index, yearly_gross.values, marker='o', linestyle='-', color='green')
plt.title("Загальний дохід фільмів за роками")
plt.xlabel("Рік")
plt.ylabel("Загальний дохід (USD)")
plt.grid(True)
plt.show()


#-----


df['main_genre'] = df['genres'].apply(lambda x: eval(x)[0] if pd.notnull(x) and len(eval(x)) > 0 else None)

genre_counts = df['main_genre'].value_counts().dropna()

plt.figure(figsize=(10, 5))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Розподіл фільмів за жанрами")
plt.axis('equal')
plt.show()
