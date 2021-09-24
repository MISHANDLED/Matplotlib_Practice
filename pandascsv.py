import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

data = pd.read_csv("DataFiles/datafile1.csv")
ids = data['Responder_id']
lang = data['LanguagesWorkedWith']

languages = []
counter = []
lang_count = Counter()

for lan in lang:
    lang_count.update(lan.split(';'))

for item in lang_count.most_common(15):
    languages.append(item[0])
    counter.append(item[1])

plt.barh(languages, counter, color="#30ab40", label="Language Users")
plt.xlabel("No. of Programmers Using")
plt.title("Language vs Users")
plt.tight_layout()
plt.show()

