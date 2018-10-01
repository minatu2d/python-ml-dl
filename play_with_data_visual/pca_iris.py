import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()

print(iris.data.shape)
print(iris.target)
X_reduced = PCA(n_components=2).fit_transform(iris.data)
print(X_reduced.shape)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=iris.target)
plt.savefig("pca_iris_reduced_2D.png")
plt.show()
