import cv2              # import library open cv atau cv2
import numpy as np        # import library numpy dengan variabel np
from skimage import data  # di library skimage import library data
# import library matplotlib.pyplot dengan variabel plt
import matplotlib.pyplot as plt
# %matplotlib inline


# membuat variabel baru dengan menggunakan skimage datya camera
img = cv2.imread('Scikit.Image/Rei.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img)
# membuat variabel row, coloumn dengan menghitung array nya menggunakan fungsi img.shape
row, column = img.shape

# membuat variabel img1 dengan menggunakan fungsi np.zeros untuk Kembalikan array baru dari bentuk dan jenis yang diberikan, diisi dengan nol.
img1 = np.zeros((row, column), dtype='uint8')


min_range = 10  # membuat variabel baru min_range dengan isi 10
max_range = 60  # membuat variabel baru min_range dengan isi 60


for i in range(row):            # untuk variabel i dengan range array 0
    for j in range(column):     # untuk variabel j dengan range array 1
        # jika img dengan [i, j] lebih dari min_range dan img [i,j] kurang dari max range
        if img[i, j] > min_range and img[i, j] < max_range:
            img1[i, j] = 255  # variabel img1[i, j] nilai nya 255
        else:  # jika tidak maka nilai nya akan 0
            img1[i, j] = 0

# membuat variabel fig, axes dengan fungsi plt.subplots(2, 2, figsize = (12,12))
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
# variabel ax dengan fungsi ravel mengubah bentuk matriks, misal dari ukuran (m, n) menjadi (n, m)
ax = axes.ravel()

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[0].imshow(img, cmap=plt.cm.gray)
# dengan array 0 dengan judul citra input
ax[0].set_title("Citra Input")
# dengan array 1 untuk membuang data dalam x dan menghitung jumlah nilai di setiap kotak, lalu menggambar distribusinya sebagai BarContainer atau Polygon. Parameter bins, range, density, dan weights diteruskan ke numpy.histogram.
ax[1].hist(img.ravel(), bins=256)
# dengan array 1 dengan judul histogram input
ax[1].set_title('Histogram Input')

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[2].imshow(img1, cmap=plt.cm.gray)
# dengan array 0 dengan judul citra input
ax[2].set_title("Citra Output")
# dengan array 1 untuk membuang data dalam x dan menghitung jumlah nilai di setiap kotak, lalu menggambar distribusinya sebagai BarContainer atau Polygon. Parameter bins, range, density, dan weights diteruskan ke numpy.histogram.
ax[3].hist(img1.ravel(), bins=256)
# dengan array 1 dengan judul histogram input
ax[3].set_title('Histogram Output')

plt.show()              # fungsi untuk memperlihatkan hasil
