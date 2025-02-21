import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_fractal(width, height, xmin, xmax, ymin, ymax, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    fractal = np.zeros((height, width), dtype=int)

    for row in range(height):
        for col in range(width):
            c = x[col] + 1j * y[row]
            fractal[row, col] = mandelbrot(c, max_iter)
    return fractal

def plot_fractal(fractal, cmap='viridis'):
    plt.figure(figsize=(10, 10))
    plt.imshow(fractal, cmap=cmap, extent=(-2, 1, -1.5, 1.5))
    plt.colorbar(label='Iterations')
    plt.title('Mandelbrot Fractal')
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    plt.show()

# Parameters
width, height = 800, 800
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 100

# Generate and plot the fractal
fractal = generate_fractal(width, height, xmin, xmax, ymin, ymax, max_iter)
plot_fractal(fractal, cmap='hot')