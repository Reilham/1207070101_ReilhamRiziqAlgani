# import library matplotlib.pyplot dengan menggunakan variabel plt
import matplotlib.pyplot as plt
# %matplotlib inline

from skimage import data  # dari library skimage dengan meingimport library data
from skimage.io import imread  # dari library skimage.io import library imread
from skimage.color import rgb2gray  # dari skimage.color import lubrary rgb2gray
import numpy as np  # import library numpy dengan variabel np

# membuar variabel baru citra1 dengan menggunakan fungsi imread dengan file name mobil.tif
citra1 = imread(fname="mobil.tif")
# membuar variabel baru citra1 dengan menggunakan fungsi imread dengan file name boneka2.tif
citra2 = imread(fname="boneka2.tif")

# menampilkan array citra 1 dengan menggunakan fungsi citra1.shape
print('Shape citra 1 : ', citra1.shape)
# menampilkan array citra 1 dengan menggunakan fungsi citra2.shape
print('Shape citra 2 : ', citra2.shape)

# membuat variabel fig, axes dengan fungsi plt.subplots(2, 2, figsize = (10,10))
fig, axes = plt.subplots(1, 2, figsize=(10, 10))
# variabel ax dengan fungsi ravel mengubah bentuk matriks, misal dari ukuran (m, n) menjadi (n, m)
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')       # Menampilkan citra 1
ax[0].set_title("Citra 1")              # Memberikan judul pada citra 1
ax[1].imshow(citra2, cmap='gray')       # Menampilkan citra 2
ax[1].set_title("Citra 2")              # Memberikan judul pada citra 2

# proses filter rerata untuk citra mobil
# F2 = double(inputMobil);
# for baris=2 : tinggiA-1
#    for kolom=2 : lebarA-1
#        jum = F2(baris-1, kolom-1)+ F2(baris-1, kolom) + F2(baris-1, kolom-1) + ...
#              F2(baris, kolom-1) + F2(baris, kolom) + F2(baris, kolom+1) + ...
#              F2(baris+1, kolom-1) + F2(baris+1, kolom) + F2(baris+1, kolom+1);
#         outputMobil(baris, kolom) = uint8(1/9 * jum);
#    end
# end

# Meng-copy citra 1 ke variabel copyCitra1 dan mengubah tipe datanya menjadi float
copyCitra1 = citra1.copy().astype(float)
# Meng-copy citra 2 ke variabel copyCitra2 dan mengubah tipe datanya menjadi float
copyCitra2 = citra2.copy().astype(float)

m1, n1 = copyCitra1.shape           # Mendapatkan ukuran baris dan kolom citra 1
# Membuat array kosong dengan ukuran yang sama dengan citra 1 untuk menyimpan hasil akhir
output1 = np.empty([m1, n1])


m2, n2 = copyCitra2.shape      # Mendapatkan ukuran baris dan kolom citra 2
# Membuat array kosong dengan ukuran yang sama dengan citra 2 untuk menyimpan hasil akhir
output2 = np.empty([m2, n2])
# Menampilkan dimensi copyCitra1
print('Shape copy citra 1 : ', copyCitra1.shape)
# Menampilkan dimensi output1
print('Shape output citra 1 : ', output1.shape)

print('m1 : ', m1)          # Menampilkan nilai m1 (jumlah baris citra 1)
print('n1 : ', n1)          # Menampilkan nilai n1 (jumlah kolom citra 1)
print()

# Menampilkan dimensi copyCitra2
print('Shape copy citra 2 : ', copyCitra2.shape)
# Menampilkan dimensi output2
print('Shape output citra 3 : ', output2.shape)
print('m2 : ', m2)       # Menampilkan nilai m2 (jumlah baris citra 2)
print('n2 : ', n2)         # Menampilkan nilai n2 (jumlah kolom citra 2)
print()

# Proses Filter Rerata Pada Citra Input 1
for baris in range(0, m1-1):        # Melakukan perulangan sebanyak jumlah baris citra 1
    for kolom in range(0, n1-1):    # Melakukan perulangan sebanyak jumlah kolom citra 1
        a1 = baris  # variabel a1 sama dengan baris
        a1 = baris  # variabel a1 sama dengan baris
        b1 = kolom  # variabel 1 sama dengan baris
        jumlah = copyCitra1[a1-1, b1-1] + copyCitra1[a1-1, b1] + copyCitra1[a1-1, b1-1] + \
            copyCitra1[a1, b1-1] + copyCitra1[a1, b1] + copyCitra1[a1, b1+1] + \
            copyCitra1[a1+1, b1-1] + \
            copyCitra1[a1+1, b1] + copyCitra1[a1+1, b1 +
                                              1]           # Menghitung jumlah piksel dalam jendela 3x3
        # Menghitung nilai rerata dan memasukkan hasilnya ke dalam output1
        output1[a1, b1] = (1/9 * jumlah)

# Proses Filter Rerata Pada Citra Input 2
for baris1 in range(0, m2-1):       # Melakukan perulangan sebanyak jumlah baris citra 2
    for kolom1 in range(0, n2-1):   # Melakukan perulangan sebanyak jumlah kolom citra 2
        a1 = baris1  # variabel a1 sama dengan kolom1
        a1 = baris1  # variabel a1 sama dengan kolom1
        b1 = kolom1  # variabel b1 sama dengan baris1
        jumlah = copyCitra2[a1-1, b1-1] + copyCitra2[a1-1, b1] + copyCitra2[a1-1, b1-1] + \
            copyCitra2[a1, b1-1] + copyCitra2[a1, b1] + copyCitra2[a1, b1+1] + \
            copyCitra2[a1+1, b1-1] + \
            copyCitra2[a1+1, b1] + copyCitra2[a1+1, b1 +
                                              1]     # Menghitung jumlah piksel dalam jendela 3x3
        # Menghitung nilai rerata dan memasukkan hasilnya ke dalam output2
        output2[a1, b1] = (1/9 * jumlah)

# membuat variabel fig, axes dengan fungsi plt.subplots(2, 2, figsize = (10,10))
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
# variabel ax dengan fungsi ravel mengubah bentuk matriks, misal dari ukuran (m, n) menjadi (n, m)
ax = axes.ravel()

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[0].imshow(citra1, cmap='gray')
# dengan array 0 dengan judul citra input 1
ax[0].set_title("Input Citra 1")

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[1].imshow(citra2, cmap='gray')
# dengan array 0 dengan judul citra input 1
ax[1].set_title("Input Citra 1")

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[2].imshow(output1, cmap='gray')
# dengan array 0 dengan judul OUTPUT citra input 1
ax[2].set_title("Output Citra 1")

# Untuk menampilkan gambar skala abu-abu atur colormapping menggunakan parameter cmap='gray', vmin=0, vmax=255.
ax[3].imshow(output2, cmap='gray')
# dengan array 0 dengan judul OUTPUT citra input 2
ax[3].set_title("Output Citra 2")
plt.show()
