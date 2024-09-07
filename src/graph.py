import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from compare import scrapeProducts

# Set the 3D graph
fig = plt.figure(figsize=(10, 10))
plot = plt.axes(projection='3d')
axis = [5, 5, 5]
data = np.ones(axis)
transparency = 0.9
 
# Control colors
colors = np.empty(axis + [4])
colors[0] = [1, 0, 0, transparency]
colors[1] = [0, 1, 0, transparency]  
colors[2] = [0, 0, 1, transparency]
colors[3] = [1, 1, 0, transparency]
colors[4] = [1, 1, 1, transparency]
 
# turn off/on axis
plt.axis('off')
plot.voxels(data, facecolors=colors, edgecolors='grey')
plt.show()