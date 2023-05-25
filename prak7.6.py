# dari skimage.color import lubrary rgb2gray
from skimage.color import rgb2gray
import cv2      # import library open cv atau cv2
import numpy as np              # import library numpy dengan variabel np
# dari library skimage.io import library imread
from skimage.io import imread
# dari library skimage dengan meingimport library data
from skimage import data
# import library matplotlib.pyplot dengan variabel plt
import matplotlib.pyplot as plt
# %matplotlib inline

# Load Image
# Membaca gambar dengan nama file "mahe.jpg" dan menyimpannya dalam variabel citra1
citra1 = imread(fname="gedung.tif")
print(citra1.shape)         # Menampilkan dimensi gambar citra1

# Menampilkan gambar citra1 dengan peta warna abu-abu
plt.imshow(citra1, cmap='gray')

# Membuat kernel konvolusi dengan matriks 3x3
kernel = np.array([[-1, 0, -1],
                   [0, 4, 0],
                   [-1, 0, -1]])


# Melakukan konvolusi citra1 dengan kernel yang telah dibuat
citraOutput = cv2.filter2D(citra1, -1, kernel)


# membuat variabel fig, axes dengan fungsi plt.subplots(2, 2, figsize = (12,12))
fig, axes = plt.subplots(1, 2, figsize=(12, 12))
# variabel ax dengan fungsi ravel mengubah bentuk matriks, misal dari ukuran (m, n) menjadi (n, m)
ax = axes.ravel()

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[0].imshow(citra1, cmap='gray')
# dengan array 0 dengan judul citra input
ax[0].set_title("Citra Input")
# dengan array 1 untuk membuang data dalam x dan menghitung jumlah nilai di setiap kotak, lalu menggambar distribusinya sebagai BarContainer atau Polygon. Parameter bins, range, density, dan weights diteruskan ke numpy.histogram.
ax[1].imshow(citraOutput, cmap='gray')
# dengan array 1 dengan judul histogram input
ax[1].set_title("Citra Output")
plt.show()                       # fungsi untuk memperlihatkan hasil
