# # This is a sample Python script.
#
import math


def euclideces_btpoints_distance(x_coordinates_1, x_coordinates_2, y_coordinates_1, y_coordinates_2):
    """Funcja obliczająca odległość między puntami w układzie =Kartezjansim (dwuwymiarowym)"""
    return math.sqrt(math.pow(x_coordinates_1 - x_coordinates_2, 2) + math.pow(y_coordinates_1 - y_coordinates_2, 2))


# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# class point_object:
#     def __init__(self):
#         self.x = 1
#         self.y = 1
#     def get_point_x(self):
#         return self.x
#     def get_point_y(self):
#         return self.y
#     def set_point(self, x,y):
#         self.x=x
#         self.y=y
#
#
# def euklides_generator (point):
#     print(point.get_point_x())# Press Ctrl+F8 to toggle the breakpoint.
#     print(point.get_point_y())
# ## Wirg
# object_1 = point_object()
# euklides_generator(object_1)
#
import storage
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(12345)

coords = np.random.rand(rng.integers(low=400, high=600, size=1).item(), 2) * 100
print(coords)
x_coordinates = []
y_coordinates = []
# plt.plot(scalex=coords.)
for each in coords.tolist():
    x_coordinates.append(each[0])
    y_coordinates.append(each[1])
print(x_coordinates)
print(y_coordinates)
plt.scatter(x=x_coordinates, y=y_coordinates)
plt.title("Generalizacja problemu początkowego")
plt.xlabel("Punkt szerokości geograficznej")
plt.ylabel("Punkt długości geograficznej")
plt.show()
old2 = 0
oldo = 0
for each in x_coordinates:
    for each2 in y_coordinates:
        print(each, " - ", each2)
        print("distance", euclideces_btpoints_distance(each, oldo, each2, old2))
        oldo = each
        old2 = each2
lista = [x_coordinates[0], y_coordinates[0]]
storage0 = storage(lista)
