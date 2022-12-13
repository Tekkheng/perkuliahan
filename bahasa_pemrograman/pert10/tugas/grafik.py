import matplotlib.pyplot as plt
import numpy as np

"""
Keterangan:

plt.plot(x,y) → Meletakkan posisi titik di x dan y
plt.xlabel → Keterangan sumbu horizontal
plt.ylabel → Keterangan sumbu vertikal
plt.title → Judul chart
plt.grid → Menampilkan garis grid
plt.show → Menampilkan chart
"""

t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2.5 * np.pi * t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (V)')

plt.title('Grafik Gelombang Sinus')
plt.grid(True)

plt.show()


