import matplotlib.pyplot as plt

# squares
x_values = range(1, 1000)
y_values = [x**2 for x in x_values]


plt.style.use('dark_background')
fig, ax = plt.subplots()

# color = 'red'
color = (0, 0.8, 0)
ax.scatter(x_values, y_values, c=color, s=10)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=10)
ax.set_ylabel("Square of Value", fontsize=10)

# set size of tick labels
ax.tick_params(axis='both', labelsize=20)

# set the range for each axis
ax.axis([0, 1100, 0, 1000000])

# show graph
# plt.show()

# save graph to a file
plt.savefig('saved_graphs/scatter_squares.png', bbox_inches="tight")
