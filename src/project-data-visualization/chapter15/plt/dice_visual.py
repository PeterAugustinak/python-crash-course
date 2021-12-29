from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create one D6 and one D10 dice
die_1 = Die()
die_2 = Die(10)

# 15-6
die_8_1 = Die(8)
die_8_2 = Die(8)

# 15-7
die_6_1 = Die()
die_6_2 = Die()
die_6_3 = Die()

# 15-8
die_12_1 = Die(12)
die_12_2 = Die(12)


# make some rolls and store results in a list
roll_times = 100_000
# result = [die_1.roll() + die_2.roll() for _ in range(roll_times)]
# 15-6
# result = [die_8_1.roll() + die_8_2.roll() for _ in range(roll_times)]
# 15-7
# result = [die_6_1.roll() + die_6_2.roll() + die_6_3.roll() for _ in
#           range(roll_times)]
# 15-8
result = [die_12_1.roll() * die_12_2.roll() for _ in range(roll_times)]

# analyze the result
# max_results = die_1.num_sides + die_2.num_sides
# 15-6
# max_results = die_8_1.num_sides + die_8_2.num_sides
# 15-7
# max_results = die_6_1.num_sides + die_6_2.num_sides + die_6_3.num_sides
# 15-8
max_results = die_12_1.num_sides * die_12_2.num_sides

frequencies = [result.count(value) for value in set(result)]
# print(frequencies)

# visualize the results
# x_values = list(range(1, max_results+1))
# 15-8
x_values = [x for x in set(result)]
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling 2 x D6 {roll_times} '
                         f'times - multiplicated result',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout},
             filename='../../visualizations/charts/d12_d12_multiply.html')
