from matplotlib import pyplot as plt
import csv
from collections import Counter

languages = []
counter = []


with open('datafile1.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    C = Counter()
    for row in reader:
        C.update(row['LanguagesWorkedWith'].split(";"))

    for item in C.most_common(15):
        languages.append(item[0])
        counter.append(item[1])

languages.reverse()
counter.reverse()
print(languages)
print(counter)

plt.barh(languages,counter, color="#30ab40", label = "Language Users")
plt.xlabel("No. of Programmers Using")
plt.title("Language vs Users")
plt.tight_layout()
plt.show()
