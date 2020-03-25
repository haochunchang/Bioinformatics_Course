#!/Users/haochunchang/opt/miniconda3/envs/bioinfo/bin/python3
"""
Example for clustering

"""
import numpy as np

from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import seaborn as sns


def generate_random_2D_data(filepath):
    
    X = -2 * np.random.rand(100,2)
    X1 = 1 + 2 * np.random.rand(50,2)
    X[50:100, :] = X1

    np.savetxt(filepath, X)


if __name__ == "__main__":
    
    filepath = "example_cluster_data.txt"
    
    generate_random_2D_data(filepath)
    X = np.loadtxt(filepath)
    
    num_cluster = 2
    cluster = KMeans(n_clusters=num_cluster)
    cluster.fit(X)
    print(cluster)
    
    sns.scatterplot(X[ : , 0], X[ :, 1], 
                hue=cluster.labels_,
                palette=sns.color_palette('dark', num_cluster),
                s=30, alpha=0.8)

    for i in range(num_cluster):
        plt.scatter(cluster.cluster_centers_[i, 0],
                    cluster.cluster_centers_[i, 1], 
                    s=200, c='tab:red', marker='P')

#     plt.savefig("example_data_KMeans_{}.png".format(num_cluster), 
#                 dpi=150, bbox_inches='tight')
    plt.show()
    plt.close()