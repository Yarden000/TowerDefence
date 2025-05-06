import matplotlib.pyplot as plt
import svgelements
from svgelements import Path, Line, Arc, CubicBezier, QuadraticBezier, Close, Move



# Define the path using svgelements
path = Path(
    Move((100, 100)),  # Move to (100, 100)
)

# Append a quadratic Bézier curve
path.append(QuadraticBezier((200, 300), (0, 200), (200, 400)))
path.append(CubicBezier((200, 400), (0, 200), (500, 500), (300, 600)))

points = [(200, 300), (0, 200), (200, 400), (200, 400), (0, 200), (500, 500), (300, 600)]

# Prepare the plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)

# Extract points from the path and plot them
'''
for segment in path:
    if isinstance(segment, Line):
        x_values = [segment.start.real, segment.end.real]
        y_values = [segment.start.imag, segment.end.imag]
        ax.plot(x_values, y_values, marker='o', color='b')
    elif isinstance(segment, QuadraticBezier):
        # Approximate the quadratic Bézier curve by sampling points
        t_values = [i / 100 for i in range(101)]
        x_values = [segment.point(t).real for t in t_values]
        y_values = [segment.point(t).imag for t in t_values]
        ax.plot(x_values, y_values, color='g')
'''
t_values = [i / 100 for i in range(101)]
x_values = [path.point(t, 1000000).real for t in t_values]
y_values = [path.point(t, 1000000).imag for t in t_values]
ax.plot(x_values, y_values, 'g.')


x_values = [point[0] for point in points]
y_values = [point[1] for point in points]
ax.plot(x_values, y_values, 'r.')


# Display the plot
plt.title("SVG Path Visualization")
plt.show()
