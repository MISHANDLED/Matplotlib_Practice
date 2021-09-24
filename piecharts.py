import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

# Data Reading
data = pd.read_csv("DataFiles/datafile1.csv")
ids = data['Responder_id']
lang = data['LanguagesWorkedWith']

# Variables
languages = []
counter = []
explode = [0, 0, 0.2, 0, 0]
lang_count = Counter()

for lan in lang:
    lang_count.update(lan.split(';'))

for item in lang_count.most_common(5):
    languages.append(item[0])
    counter.append(item[1])


plt.pie(counter, labels=languages, explode=explode, startangle=90, autopct="%1.1f%%", wedgeprops={'edgecolor': 'black'})
plt.show()
