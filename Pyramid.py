from matplotlib import pyplot as plt

slices = [70, 20, 10]
labels = ['Sky', 'Pyramid', 'Other Side of Pyramid']
colors = ['#1f77b4', '#fff44f', '#9F7D4F']
plt.pie(slices, startangle=335, labels=labels, colors=colors)
plt.savefig('logic.png')
plt.show()

# Random Fun with Pie Charts