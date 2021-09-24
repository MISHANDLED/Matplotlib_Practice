from matplotlib import pyplot as plt
import numpy as np

# Variables
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

x_index = np.arange(len(ages_x))
print(x_index)

# Defining the Plot
plt.bar(x_index-0.25, dev_y, color='#abc', width=0.25, label="All Devs")
plt.bar(x_index, py_dev_y, color='#008000', width=0.25, label="Python Devs")
plt.bar(x_index+0.25, js_dev_y, color='#000', width=0.25, label="JavaScript Devs")

# Putting Labels and Title of The Plot
plt.xticks(ticks=x_index, labels=ages_x)
plt.xlabel("HELLO-1")
plt.ylabel("WORLD-1")
plt.title("TITLE-1")
plt.legend()
plt.show()
