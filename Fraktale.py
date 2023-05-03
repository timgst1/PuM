import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iters):
    z = c
    for n in range(max_iters):
        if np.abs(z) > 2:
            return n
        z = z*z + c
    return max_iters

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iters):
    x, y = np.meshgrid(np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height))
    c = x + 1j * y
    n3 = np.empty((width, height))
    n3 = np.where(np.abs(c) <= 2, mandelbrot(c, max_iters), max_iters)
    return (x, y, n3)

xmin, xmax, ymin, ymax = -2, 1, -1, 1
width, height = 500, 500
max_iters = 100
x, y, n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iters)

plt.imshow(n3, extent=[xmin, xmax, ymin, ymax])
plt.show()
