from matplotlib import pyplot as plt
import pandas as pd

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
# bins = [10, 20, 30, 40, 50, 60, 70]
# plt.hist(ages, bins=bins, edgecolor='Black')
# plt.show()

# Data Reading
data = pd.read_csv('DataFiles/datafile3.csv')
id = data['Responder_id']
age = data['Age']
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(age, bins=bins, edgecolor="Black", log=True)

# Median Line
plt.axvline(age.median(), color="#12fc2d", label="Median Age", linewidth=5)

plt.xlabel("Ages")
plt.ylabel("Count")
plt.legend()

plt.tight_layout()
plt.show()
