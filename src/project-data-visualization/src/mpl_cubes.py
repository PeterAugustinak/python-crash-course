# 15-1

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)

# set chart title and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()

# save file
# plt.savefig('saved_graphs/plot_cubes.png')
