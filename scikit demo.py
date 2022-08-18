# Python program to demonstrate
# KNN classification algorithm
# on IRIS dataset

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

iris_dataset=load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], train_size = 0.95, random_state = 4)

kn = KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train, y_train)
print("Test score: {:.2f}".format(kn.score(X_test, y_test)))

x_new = np.array([[5, 2.9, 1, 0.2]])
prediction = kn.predict(x_new)

print("Voorspelde soort: " + str(iris_dataset["target_names"][prediction]))   # printen welk type bloem er voorspeld wordt