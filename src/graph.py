import plotly.graph_objects as go


def draw_box(length, width, height):
    # Define the vertices of the box
    x = [0, 0, length, length, 0, 0, length, length]
    y = [0, width, width, 0, 0, width, width, 0]
    z = [0, 0, 0, 0, height, height, height, height]

    # Defining more triangles to cover each face better
    fig = go.Figure(data=[go.Mesh3d(
        x=x,
        y=y,
        z=z,
        # Define the twelve triangles for the six faces of the box
        i=[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7],  # First vertices of triangles
        j=[1, 2, 4, 2, 3, 5, 3, 6, 7, 0, 7, 6, 5, 6, 7, 6, 7, 4, 7, 4, 5, 5, 4, 6],  # Second vertices of triangles
        k=[2, 4, 5, 3, 5, 6, 0, 4, 6, 0, 5, 7, 0, 7, 6, 1, 3, 7, 1, 0, 4, 1, 5, 0],  # Third vertices of triangles
        color='red',  # Solid red color
        opacity=1,    # Fully opaque
        flatshading=True,  # Ensures a smooth look
        showscale=False  # Hide the color scale legend
    )])

    # Hide grid, axes, and box background
    fig.update_layout(scene=dict(
        xaxis=dict(showbackground=False, showgrid=False, visible=False),
        yaxis=dict(showbackground=False, showgrid=False, visible=False),
        zaxis=dict(showbackground=False, showgrid=False, visible=False)
    ))

    # Show the plot
    fig.show()

# Example: 10 inches (length), 5 inches (width), 4 inches (height)
draw_box(10, 5, 4)