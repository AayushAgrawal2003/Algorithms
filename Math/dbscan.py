import numpy as np 
import math
import random
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs

points = 400
X, y = make_blobs(n_samples=points, centers = 2, cluster_std=0.60, random_state=4)

x = list(X[:,0])
y = list(X[:,1])


