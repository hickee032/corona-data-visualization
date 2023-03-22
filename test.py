import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()

line = plt.plot([], [],
                color='skyblue',
                marker='o', markerfacecolor='blue',
                markersize=6)[0]
plt.xlim(0, 6)
plt.ylim(10, 16)

list_x = []
list_y = []

def update(x_coordinate):
    list_x.append(x_coordinate)
    list_y.append(x_coordinate + 10)

    line.set_data(list_x, list_y)

graph_ani = FuncAnimation(fig=fig, func=update, frames=[1, 2, 3, 4, 5])
graph_ani.save('graph_ani.gif', writer='imagemagick', fps=3, dpi=100)

plt.show()