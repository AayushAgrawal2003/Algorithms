import numpy as np 
import math
import random
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=400, centers = 4, cluster_std=0.9, random_state=16)

x = list(X[:,0])
y = list(X[:,1])
points = 400
# for i in range(points):
#     x.append(random.randint(1,20))
#     y.append(random.randint(1,20))

#plt.scatter(x,y)

# Figure how to get a k valuesx
k = 4
centroid_x = []
centroid_y = []
for i in range(k):
    centroid_x.append(random.uniform(min(x),max(x)))
    centroid_y.append(random.uniform(min(y),max(y)))
# plt.scatter(centroid_x,centroid_y)
# plt.show()

# Assign clusters to each point and then use this to get next centroids 
iterations = 20

colors = ["#ff7f0e" , "#1f77b4" , "tan" , "slateblue"]

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

arr = [[[],[]],[[],[]], [[],[]],[[],[]]]

for l in range(iterations):
    for i in range(points):
        min = 1000
        for j in range(k):
            if dist(centroid_x[j],centroid_y[j],x[i],y[i]) < min:
                index = j
                min = dist(centroid_x[j],centroid_y[j],x[i],y[i])
        arr[index][0].append(x[i])
        arr[index][1].append(y[i])
        plt.scatter(x[i],y[i], color = colors[index])
    plt.scatter(centroid_x,centroid_y, color = "#2ca02c")
    plt.show()
    print(centroid_x)
    for j in range(k):
        centroid_x[j] = sum(arr[j][0]) / len(arr[j][0])
        centroid_y[j] = sum(arr[j][1]) / len(arr[j][1])

    sarr = [[[],[]],[[],[]], [[],[]],[[],[]]]
    



        


    

