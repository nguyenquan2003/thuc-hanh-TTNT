import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importing for 3D plotting
from scipy.spatial.distance import cdist

def initialize_centers(X, n_cluster):
    return X[np.random.choice(X.shape[0], n_cluster, replace=False)]

def predict_labels(X, centers):
    distances = cdist(X, centers)
    return np.argmin(distances, axis=1)

def update_centers(X, labels, n_cluster):
    centers = np.zeros((n_cluster, X.shape[1]))
    for k in range(n_cluster):
        Xk = X[labels == k, :]
        centers[k, :] = np.mean(Xk, axis=0)
    return centers

def has_converged(centers, new_centers):
    return np.array_equal(centers, new_centers)

def visualize_clusters_3d(X, centers, labels, n_cluster, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.title(title)
    plt_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    for i in range(n_cluster):
        data = X[labels == i]
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=plt_colors[i], marker='^', label='cluster_' + str(i))
        ax.scatter(centers[i][0], centers[i][1], centers[i][2], c=plt_colors[i + 4], marker='o', s=100, label='center_' + str(i))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend()
    plt.show()

# Generate initial 3D data
means_3d = [[2, 2, 2], [9, 2, 2], [4, 9, 4]]
cov_3d = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
n_samples_3d = 500
n_cluster_3d = 3
X0_3d = np.random.multivariate_normal(means_3d[0], cov_3d, n_samples_3d)
X1_3d = np.random.multivariate_normal(means_3d[1], cov_3d, n_samples_3d)
X2_3d = np.random.multivariate_normal(means_3d[2], cov_3d, n_samples_3d)
X_3d = np.concatenate((X0_3d, X1_3d, X2_3d), axis=0)

# Visualize initial 3D data
visualize_clusters_3d(X_3d, np.zeros((n_cluster_3d, 3)), np.zeros(X_3d.shape[0]), n_cluster_3d, 'Initial 3D Data')

# Run K-means in 3D
def kmeans(init_centers, init_labels, X, n_cluster):
    centers = init_centers
    labels = init_labels
    times = 0
    while True:
        labels = predict_labels(X, centers)
        visualize_clusters_3d(X, centers, labels, n_cluster, 'Assigned label for data at time = ' + str(times + 1))
        new_centers = update_centers(X, labels, n_cluster)
        if has_converged(centers, new_centers):
            break
        centers = new_centers
        visualize_clusters_3d(X, centers, labels, n_cluster, 'Update center position at time = ' + str(times + 1))
        times += 1
    visualize_clusters_3d(X, centers, labels, n_cluster, 'Final Clusters and Centers')
    return (centers, labels, times)

# ... (rest of the code remains unchanged)

# Run K-means in 3D
init_centers_3d = initialize_centers(X_3d, n_cluster_3d)
init_labels_3d = np.zeros(X_3d.shape[0])
visualize_clusters_3d(X_3d, init_centers_3d, init_labels_3d, n_cluster_3d, 'Init centers. Assigned all data as cluster 0')
centers_3d, labels_3d, times_3d = kmeans(init_centers_3d, init_labels_3d, X_3d, n_cluster_3d)
print('Done! Kmeans has converged after', times_3d, 'times')
print('Final centers:', centers_3d)