# test_apple_style.py
import botionplotlib  # Apply style once
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Ensure a compatible backend for animations
plt.switch_backend('TkAgg')  # Use TkAgg for animation support

# Data setup
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)
X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
Z = np.sin(np.sqrt(X**2 + Y**2))

# 1. Line Plot
plt.figure()
plt.plot(x, y, label='Sine')
plt.plot(x, z, label='Cosine')
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# 2. Scatter Plot
plt.figure()
plt.scatter(x, y, label='Sine Points')
plt.scatter(x, z, label='Cosine Points')
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# 3. Bar Plot
plt.figure()
plt.bar(x[:10], y[:10], label='Sine Bars')
plt.title('Bar Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# 4. Histogram
plt.figure()
plt.hist(y, bins=20, label='Sine Dist')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)

# 5. Heatmap
plt.figure()
plt.imshow(Z)
plt.title('Heatmap')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()

# 6. Contour Plot
plt.figure()
plt.contour(X, Y, Z, levels=10)
plt.contourf(X, Y, Z, levels=10, cmap='apple_cmap')
plt.title('Contour Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# 7. 3D Surface Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='apple_cmap')  # Explicitly set cmap
ax.set_title('3D Surface Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 8. Pie Chart
plt.figure()
plt.pie([30, 20, 50], labels=['A', 'B', 'C'], autopct='%1.1f%%')
plt.title('Pie Chart')

# 9. Box Plot
plt.figure()
plt.boxplot([y, z], labels=['Sine', 'Cosine'])
plt.title('Box Plot')
plt.ylabel('Value')
plt.grid(True)

# 10. Animation
fig, ax = plt.subplots()
line, = ax.plot([], [], label='Animated Sine')
ax.set_title('Animation')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.legend()
ax.grid(True)

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(x), interval=50, blit=True)

plt.show()