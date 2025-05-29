import matplotlib.pyplot as plt #Import pyplot

# Приклад данних
week_days = ['Monday', 'Tuesday', 'Wednasday', 'Thursday', 'Friday']
income = [0, 100, 1000, 1500, 2000]

#(colors)
colors = ['red', 'orange', 'yellow', 'purple', 'black']

# Барра графіку
plt.bar(week_days, income, color=colors)


# Підпіси
plt.title('Income in a week')
plt.xlabel('Day of the week')
plt.ylabel('Income')
# Showing
plt.show()
