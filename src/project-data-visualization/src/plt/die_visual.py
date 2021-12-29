from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create a D6
die = Die()

# make some rolls and store results in a list
roll_times = 1000
result = [die.roll() for _ in range(roll_times)]

# analyze the result
frequencies = [result.count(value) for value in set(result)]
# print(frequencies)

# visualize the results
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling one D6 {roll_times} times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='graphs/d6.html')
