import pandas as pd
from matplotlib import pyplot as plt

# Data Reading
data = pd.read_csv("DataFiles/datafile2.csv")

# Variables
AGES_X = data['Age']
devsal = data['All_Devs']
pytsal = data['Python']
jvssal = data['JavaScript']

# Plotting
plt.plot(AGES_X, devsal, color="#444123", label='All Dev Salaries')
plt.plot(AGES_X, pytsal, color="#000080", label='Python Salaries')

plt.legend()
plt.xlabel("AGE")
plt.ylabel("SALARY")

# plt.fill_between(AGES_X, pytsal, 50000, where=pytsal > 50000, interpolate=True, color='#123456', alpha=0.25)
# plt.fill_between(AGES_X, pytsal, 50000, where=pytsal < 50000, interpolate=True, color='red')

plt.fill_between(AGES_X, pytsal, devsal, where=pytsal > 50000, interpolate=True, color='#123456', alpha=0.25)
plt.fill_between(AGES_X, pytsal, devsal, where=pytsal < 50000, interpolate=True, color='red')

# Used For Coloring From Y Axis
# plt.fill_betweenx(devsal,AGES_X)

plt.tight_layout()
plt.show()

