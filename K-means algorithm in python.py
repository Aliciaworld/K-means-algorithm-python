import random


# First define the main function, which give the skeleton of the algorithm
def main(data, k):
    centroids = initial_centroids(data, k)
    while True:
        old_centroids = centroids
        labels = get_labels(data, centroids)
        centroids = update_centroids(data, labels)

        if stop(old_centroids, centroids):
            break

    return labels


# Define the helping functions (the data can be multi-dimensional points).
# Here only use two-dimensional points as examples, and we will define:
# 1. initial_centroids()
# 2. get_labels()
# 3. update_centroids()
# 4. stop()

# 1. initial_centroids()
def initial_centroids(data, k):
    # line 19-25 are to find the min and max x and y in data
    x_min = y_min = float('inf')
    x_max = y_max = float('-inf')
    for point in data:
        x_min = min(point[0], x_min)
        x_max = max(point[0], x_max)
        y_min = min(point[1], y_min)
        y_max = max(point[1], y_max)

    centroids = []
    for i in range(k):
        centroids.append([random_centroids(x_min, x_max), random_centroids(y_min, y_max)])

    return centroids


# This random_centroids is another helping function to the initial_centroids function
# 1.1 random_centroids()
def random_centroids(small, large):
    return small + (large - small) * random.random()


# 2. get_labels()
def get_labels(data, centroids):
    labels = []
    for point in data:
        min_distance = float('inf')
        label = None
        for i, centroid in enumerate(centroids):
            new_distance = get_distance(point, centroid)
            if min_distance > new_distance:
                min_distance = new_distance
                label = i
            labels.append(label)
    return labels


# 2.1 get_distance(point1,point2)
def get_distance(point1, point2):
    return((point1[0] - point2[2])**2 + (point1[1] - point2[2])**2) ** 0.5


# 3. update_centroids()
def update_centroids(data, labels):
    new_centroids = []
    counts = []

    v = dict(zip(labels, data))
    for label, point in v.items():
        v[label][0] += point[0]
        v[label][1] += point[1]
        new_centroids.append(v[label])
        counts.append(len(v[label]))

    for i, (x, y) in enumerate(new_centroids):
        new_centroids[i] = (x/counts[i], y/counts[i])
    return new_centroids


# 4. stop()
def stop(old_centroids, new_centroids, threshold=1e-5):
    total_movement = 0
    for old, new in zip(old_centroids, new_centroids):
        total_movement += get_distance(old, new)
        if total_movement < threshold:
            break
    return 'K-means algorithm optimised done'
