from matplotlib import pyplot as plt
import pandas as pd

# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
# plt.scatter(x, y, s=sizes, c=colors, marker='o', cmap="Greens", edgecolors="Black")
# color_bar = plt.colorbar()
# color_bar.set_label("LEVELS")
# plt.show()

# Data Reading
data = pd.read_csv("datafile4.csv")

# Variables
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']
plt.scatter(view_count, likes, c=ratio, cmap='summer', edgecolor='black', linewidth=1)

# Color Palate Set
color_bar = plt.colorbar()
color_bar.set_label('Like/Dislike Ratio')

# Using Log Scale
plt.xscale("log")
plt.yscale("log")

# LEGENDS
plt.title('Trending YouTube Videos')
plt.xlabel("View Count")
plt.ylabel("Likes")
plt.legend()

plt.tight_layout()
plt.show()
