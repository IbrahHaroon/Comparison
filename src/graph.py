import plotly.graph_objects as go 
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_voxels_matplotlib(nx, ny, nz):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Define a 3D array of the specified shape filled with `True` (occupied voxels)
    voxels = np.ones((nx, ny, nz), dtype=bool)

    # Define colors for the voxels (all blue)
    colors = np.full(voxels.shape, 'blue', dtype=object)

    # Plot the voxels
    ax.voxels(voxels, facecolors=colors, edgecolors='black', alpha=0.5)

    # Set labels and title
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.set_title(f"Voxel Grid: {nx} × {ny} × {nz}")

    # **Fix aspect ratio so the rectangular shape is preserved**
    ax.set_box_aspect([nx, ny, nz])  # Ensure correct aspect ratio

    plt.show()

# Call function with 10×5×2 dimensions
#plot_voxels_matplotlib(8, 8, 4)