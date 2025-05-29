import matplotlib.pyplot as plt #Import pyplot

# Приклад данних
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
income = [0, 100, 1000, 1500, 2000]

plt.plot(week_days, income)

# Підпіси
plt.title('Income in a week')
plt.xlabel('Day of the week')
plt.ylabel('Income')
# Showing
plt.show()
