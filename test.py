import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.arange(0, 2 * np.pi, np.pi / 180)  # 0 到 2 * PI，步進值 PI / 180
y = np.sin(x)

sin = pd.Series(y, index = x)   
sin.plot(title = 'y = sin(x)', xlabel = 'x', ylabel = 'y')

plt.savefig('bar_chart.png')
plt.show()
