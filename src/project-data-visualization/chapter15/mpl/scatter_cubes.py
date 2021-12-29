# 15-1, 2
import matplotlib.pyplot as plt

# cubes
x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# set chart title and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=10)
ax.set_ylabel("Cube of Value", fontsize=10)

# set size of tick labels
ax.tick_params(axis='both', labelsize=20)

# set the range for each axis
# ax.axis([0, 1100, 0, 1000000])

# show graph
plt.show()

# save graph to a file
# plt.savefig('saved_graphs/scatter_cubes.png')
