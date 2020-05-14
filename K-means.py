from sklearn.cluster import KMeans
import numpy as np

data = []
with open('./kmeans_data.dat', 'r') as f:
    for line in f.readlines():
        data.append(list(map(int,line.split())))

X = np.array(data)

# chose parameters
n_clusters = 2
predict_points = [[0, 0], [12, 3]]

print('============== cluster results ===================')          
kmeans = KMeans(n_clusters, random_state=0).fit(X) 
print(kmeans.labels_)

print('\n\n============== cluster predict ===================')    
print(kmeans.predict(predict_points))

print('\n\n============== cluster centers ===================')   
print(kmeans.cluster_centers_)
