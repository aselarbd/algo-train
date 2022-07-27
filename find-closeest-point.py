"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a list of points as a tuple (x, y) and an integer k, find the k closest points to the origin (0, 0).
"""
from math import sqrt


def closest_points(points, k):
    distance = []
    distance_map = {}
    nearest_points = []

    if len(points) <= k:
        return points
    else:
        for point in points:
            hypotenuse = sqrt(point[0] ** 2 + point[1] ** 2)
            distance.append(hypotenuse)
            distance_map[hypotenuse] = point

        distance.sort()

        for i in range(k):
            nearest_points.append(distance_map[distance[i]])

        return nearest_points


if __name__ == "__main__":
    print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
    # [(1, 2), (0, 0)]
    print(closest_points([(0, -1), (1, 2), (1, 1), (-1, -1), (3, 1)], 3))
    # [(0, -1), (-1, -1), (-1, -1)]
