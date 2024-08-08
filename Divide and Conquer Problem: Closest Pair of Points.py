import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def brute_force(points):
    min_dist = float('inf')
    pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair

def closest_pair(points):
    def closest_pair_recursive(points_sorted_x, points_sorted_y):
        if len(points_sorted_x) <= 3:
            return brute_force(points_sorted_x)

        mid = len(points_sorted_x) // 2
        midpoint = points_sorted_x[mid]

        points_left = points_sorted_x[:mid]
        points_right = points_sorted_x[mid:]

        points_left_y = list(filter(lambda x: x[0] <= midpoint[0], points_sorted_y))
        points_right_y = list(filter(lambda x: x[0] > midpoint[0], points_sorted_y))

        (dist_left, pair_left) = closest_pair_recursive(points_left, points_left_y)
        (dist_right, pair_right) = closest_pair_recursive(points_right, points_right_y)

        if dist_left < dist_right:
            min_dist = dist_left
            min_pair = pair_left
        else:
            min_dist = dist_right
            min_pair = pair_right

        strip = [p for p in points_sorted_y if abs(p[0] - midpoint[0]) < min_dist]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d = distance(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    min_pair = (strip[i], strip[j])

        return min_dist, min_pair

    points_sorted_x = sorted(points, key=lambda x: x[0])
    points_sorted_y = sorted(points, key=lambda x: x[1])
    return closest_pair_recursive(points_sorted_x, points_sorted_y)

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
min_dist, min_pair = closest_pair(points)
print("The closest pair is:", min_pair, "with a distance of:", min_dist)
