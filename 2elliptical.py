import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 3

theta = np.linspace(0, 2 * np.pi, 1000)
x = a * np.cos(theta)
y = b * np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Elliptical Orbit', color='blue')
plt.plot(0, 0, 'yo', label='Focus (Sun)')
plt.title('Elliptical Orbit with Focus')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
