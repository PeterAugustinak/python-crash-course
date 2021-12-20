import matplotlib.pyplot as plt

from random_walks import RandomWalk

# make a random walk
rw = RandomWalk(2000)

rw.fill_walk()

# plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)

# SCATTER VIEW
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
#            edgecolor='none', s=0.5)

# 15-3
# PLOT VIEW
ax.plot(rw.x_values, rw.y_values, linewidth=3)

# emphasize the first and last pints
ax.scatter(0, 0, c='green', edgecolor='none', s=500)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
           s=500)

# remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
