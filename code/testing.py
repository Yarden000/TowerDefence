from svgpathtools import Path, Line, Arc, CubicBezier, QuadraticBezier
import pygame
import matplotlib.pyplot as plt

# Define the path using svgelements
path:Path = Path()
# Append a quadratic Bézier curve
path += Path(QuadraticBezier(200 + 100j, 1 + 200j, 200 + 400j))
path += Path(CubicBezier(200 + 400j, 1 + 600j, 800 + 500j, 300 + 600j))

points = [(200, 100), (0, 200), (200, 400), (200, 400), (0, 600), (800, 500), (300, 600)]

# Prepare the plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)

# Extract points from the path and plot them

n = 50
path_len = path.length()
x_values = [path.point(path.ilength(path_len * i / n)).real for i in range(n)]
y_values = [path.point(path.ilength(path_len * i / n)).imag for i in range(n)]
ax.plot(x_values, y_values, 'g.')


x_values = [point[0] for point in points]
y_values = [point[1] for point in points]
ax.plot(x_values, y_values, 'r.')


# Display the plot
plt.title("SVG Path Visualization")
plt.show()
