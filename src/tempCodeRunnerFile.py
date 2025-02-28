def plotter(x, y, z, num_points=20):
    # Define symmetric ranges based on input dimensions
    x1 = np.linspace(-x/2, x/2, num_points)
    y1 = np.linspace(-y/2, y/2, num_points)
    z1 = np.linspace(-z/2, z/2, num_points)
    
    X, Y, Z = np.meshgrid(x1, y1, z1)
    
    values = (np.sin(X**2 + Y**2)) / (X**2 + Y**2)
    
    fig = go.Figure(data=go.Volume(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        value=values.flatten(),
        opacity=0.1,  # Adjust opacity as needed
    ))
    
    # Set the aspect ratio to match the data
    fig.update_layout(
        scene=dict(
            aspectmode='data'
        )
    )
    
    fig.show()

plotter(10.0, 5.0, 2.0)
