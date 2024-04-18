# Use this line for interactive plots in Jupyter notebooks
# %matplotlib notebook

# Use this line if running locally in an environment that supports it (like if using PyQt5 with Qt5Agg backend)
# %matplotlib qt

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Define parameters for the plot
width, height = 400, 400  # Reduced resolution for performance
frames = 60
max_iterations = 50

# Define the complex plane
x = np.linspace(-2, 2, width)
y = np.linspace(-2, 2, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y

# Function to compute Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

# Compute the Mandelbrot set
mandelbrot_set = np.zeros((height, width))
for i in range(width):
    for j in range(height):
        mandelbrot_set[j, i] = mandelbrot(C[j, i], max_iterations)

# Create the animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x, y)

def update(frame):
    ax.clear()
    ax.set_zlim(0, max_iterations)
    ax.contour3D(X, Y, mandelbrot_set, 50, cmap='viridis')  # Changed colormap to 'viridis'
    # Rotate the view
    angle = frame * (360 / frames)
    ax.view_init(30, angle)
    ax.set_title(f'Frame {frame + 1}/{frames}')
    ax.set_xlabel('Re(c)')
    ax.set_ylabel('Im(c)')
    ax.set_zlabel('Iterations')

ani = FuncAnimation(fig, update, frames=frames, interval=50)
plt.show()
