import matplotlib.pyplot as plt #Import pyplot

# Info (week days and income)
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
income = [0, 100, 1000, 1500, 2000]

#Colors
colors = ['red', 'orange', 'yellow', 'purple', 'grey', 'white']

# Circle(pie)
plt.pie(income, labels=week_days, colors=colors, autopct='%1.1f%%', startangle=90)

# Підпіси
plt.title('Income in a week')

# Axis
plt.axis('equal')

# Showing
plt.show()
