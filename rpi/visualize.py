import matplotlib.pyplot as plt
import numpy as np

name = 'Am5'

npz = np.load(f'{name}.npz')
time = npz['arr_0']
data = npz['arr_1']

plt.title(name, fontsize=16)
plt.xlabel('time')
plt.ylabel('voltage')
plt.plot(time, data, 'y')
plt.legend(['voltage'], fontsize=8)
plt.show()
