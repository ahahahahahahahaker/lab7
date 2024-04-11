import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import random
from time import perf_counter
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Задание 1
list1 = [random.random() for _ in range(1000000)]
list2 = [random.random() for _ in range(1000000)]
array_1 = np.array(list1)
array_2 = np.array(list2)

start_time = perf_counter()
result = [list1[i] * list2[i] for i in range(len(list1))]
end_time = perf_counter()
result_1 = end_time - start_time

start_time_np = perf_counter()
result_np = np.multiply(array_1, array_2)
end_time_np = perf_counter()
result_2 = end_time_np - start_time_np

print(f"Время выполнения поэлементного перемножения списков: {result_1} с")
print(f"Время выполнения поэлементного перемножения массивов:  {result_2} с")
print(f"Разница: {result_1-result_2} с")

# Задание 2
file = pd.read_csv('data1.csv', delimiter=';', encoding='cp1251')
time = file.iloc[:, 0]
position = file.iloc[:, 3]
hour_fuel = file.iloc[:, 17]
print(time, position, hour_fuel)

plt.plot(time, position, 'c', time, hour_fuel, 'm')
plt.title('График с использованем Matplotlib')
plt.xlabel('Время')
plt.ylabel('Часовой расход топлива (л\час)\n Положение дроссельной заслонки (%)')
plt.show()

plt.title('График корреляции')
plt.xlabel('Положение дроссельной заслонки (%)')
plt.ylabel('Часовой расход топлива (л\час)')
plt.plot(position, hour_fuel, 'o')
plt.show()

# Задание 3
chart_3d = plt.figure()
ax = plt.axes(projection='3d')

x = np.linspace(-5 * np.pi, 5 * np.pi, 100)
y = np.cos(x)
z = np.sin(x)

ax.scatter(x, y, z)
plt.show()

# Доп задание
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
line, = ax.plot(x, y)


def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))
    return line,


ani = animation.FuncAnimation(fig, animate, frames=100, interval=60)
writer = PillowWriter(fps=30)
plt.show()
