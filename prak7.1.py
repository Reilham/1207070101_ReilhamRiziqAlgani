import numpy as np  # import library numpy dengan variabel np
# import library matplotlib.pyplot dengan variabel plt
import matplotlib.pyplot as plt
# %matplotlib inline
import cv2  # import library open cv atau cv2
import matplotlib.image as mpimg  # import matplotlib.image denga variabel mpimg
from skimage import data  # di skimage import library data
import imageio.v3 as iio

# membuat variabel image dengan mengimport foto saya
image = cv2.imread('Scikit.Image/foto1.png', cv2.IMREAD_GRAYSCALE)
# membuat variabel baru image_equalized dengan menggunakan fungsi equalizehist untuk penyesuaian kontras dengan menggunakan histogram citra.
image_equalized = cv2.equalizeHist(image)

# membuat variabel baru CLAHE dengan menggunakan fungsi createCLAHE untuk melakukan pemerataan histogram adaptif
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))

# Apply CLAHE to the original image
image_clahe = clahe.apply(image)

# Create an empty array to store the final output
image_cs = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')

# Apply Min-Max Contrasting
min = np.min(image)
max = np.max(image)

for i in range(image.shape[0]):  # untuk variabel i dengan range array 0
    for j in range(image.shape[1]):  # untuk variabel j dengan range array 1
        # variabel image_cs i,j = 255*(image[i, j]-min)/(max-min)
        image_cs[i, j] = 255*(image[i, j]-min)/(max-min)

# membuat variabel copyCamera dengan menggunakan funsgi image.copy() dengan type data float
copyCamera = image.copy().astype(float)

# membuat variabel m1, n1 dengan menggunakan fungsi copy .shape
m1, n1 = copyCamera.shape
# membuat variabel output1 dengan fungsi np.empty yaitu digunakan untuk mengembalikan array baru dari bentuk dan tipe tertentu
output1 = np.empty([m1, n1])

for baris in range(0, m1-1):  # variabel baris dengan range array (0, m1-1)
    for kolom in range(0, n1-1):  # untuk variabel kolom dengan range array (0, n1-1)
        a1 = baris  # variabel a1 adalah baris
        b1 = kolom  # variabel b1 adalah kolom
        # membuat variabel output1[a1, b1] dengan fungsi copycamera [baris, kolom] *1.9
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9

# membuat variabel fig, axes dengan fungsi plt.subplots(5, 2, figsize = (20,20))
fig, axes = plt.subplots(5, 2, figsize=(20, 20))
ax = axes.ravel()  # variabel ax dengan fungsi ravel mengubah bentuk matriks, misal dari ukuran (m, n) menjadi (n, m)

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title("Citra Input")  # dengan array 0 dengan judul citra input
# dengan array 1 untuk membuang data dalam x dan menghitung jumlah nilai di setiap kotak, lalu menggambar distribusinya sebagai BarContainer atau Polygon. Parameter bins, range, density, dan weights diteruskan ke numpy.histogram.
ax[1].hist(image.ravel(), bins=256)
# dengan array 1 dengan judul histogram input
ax[1].set_title('Histogram Input')

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[2].imshow(image_equalized, cmap=plt.cm.gray)
# dengan array 0 dengan judul citra input HE
ax[2].set_title("Citra Output HE")
# dengan array 1 untuk membuang data dalam x dan menghitung jumlah nilai di setiap kotak, lalu menggambar distribusinya sebagai BarContainer atau Polygon. Parameter bins, range, density, dan weights diteruskan ke numpy.histogram.
ax[3].hist(image_equalized.ravel(), bins=256)
# dengan array 1 dengan judul histogram input HE Method
ax[3].set_title('Histogram Output HE Method')

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[4].imshow(image_cs, cmap=plt.cm.gray)
# dengan array 0 dengan judul citra input cs
ax[4].set_title("Citra Output CS")
# dengan array 1 untuk membuang data dalam x dan menghitung jumlah nilai di setiap kotak, lalu menggambar distribusinya sebagai BarContainer atau Polygon. Parameter bins, range, density, dan weights diteruskan ke numpy.histogram.
ax[5].hist(image_cs.ravel(), bins=256)
# dengan array 1 dengan judul histogram input HE Method
ax[5].set_title('Histogram Output CS Method')

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[6].imshow(image_clahe, cmap=plt.cm.gray)
# dengan array 0 dengan judul citra input CLAHE
ax[6].set_title("Citra Grayscale CLAHE")
# dengan array 1 untuk membuang data dalam x dan menghitung jumlah nilai di setiap kotak, lalu menggambar distribusinya sebagai BarContainer atau Polygon. Parameter bins, range, density, dan weights diteruskan ke numpy.histogram.
ax[7].hist(image_clahe.ravel(), bins=256)
# dengan array 1 dengan judul histogram OUtput CLAHE Method
ax[7].set_title('Histogram Output CLAHE Method')


# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[8].imshow(output1, cmap=plt.cm.gray)
# dengan array 0 dengan judul citra input konstanta
ax[8].set_title("Citra Grayscale Perkalian Konstanta")
# dengan array 1 untuk membuang data dalam x dan menghitung jumlah nilai di setiap kotak, lalu menggambar distribusinya sebagai BarContainer atau Polygon. Parameter bins, range, density, dan weights diteruskan ke numpy.histogram.
ax[9].hist(output1.ravel(), bins=256)
# dengan array 1 dengan judul histogram OUtput Perkalian Konstanta Method
ax[9].set_title('Histogram Output Perkalian Konstanta Method')

fig.tight_layout()  # menyesuaikan parameter subplot sehingga subplot sesuai dengan area gambar. Ini adalah fitur eksperimental
plt.show()  # fungsi untuk memperlihatkan hasil
