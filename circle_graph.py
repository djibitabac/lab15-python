# Lab13_draw_circle1.py
# Djibril Ba
# Description: This program plots a simple circle using basic math with numpy and matplotlib.
# Date: 2025-04-25

import matplotlib.pyplot as plt
import numpy as np

# Set the radius for the circle
radius = 1

# Create a list of angles from 0 to 2π
theta = np.linspace(0, 2 * np.pi, 360)

# Calculate x and y coordinates using cosine and sine
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Plot the circle
plt.plot(x, y, label='Circle', linewidth=2)

plt.title("A Simple Circle")
plt.xlabel("X-Axis")

plt.ylabel("Y-Axis")

plt.gca().set_aspect('equal', adjustable='box')  # Makes sure the circle isn't stretched
plt.legend()
plt.grid(True)

# Show the graph
plt.show()
