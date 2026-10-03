import matplotlib.pyplot as plt

import numpy as np

x = np.array([1, 2, 3, 4, 5])   
y = np.array([2, 3, 5, 7, 11])

plt.plot(x, y, color='green', linestyle='dashed', linewidth=2, markersize=12, label='Line Plot')

plt.scatter(x, y, color='red', s=100, label='Scatter Plot')

plt.title('Sample Plot')

plt.xlabel('X-axis')

plt.ylabel('Y-axis')

plt.legend()

plt.show()