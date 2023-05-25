# import library matplotlib.pyplot dengan variabel plt
import matplotlib.pyplot as plt
# %matplotlib inline

# dari library skimage dengan meingimport library data
from skimage import data
# dari library skimage.io import library imread
from skimage.io import imread
# dari skimage.color import lubrary rgb2gray
from skimage.color import rgb2gray
import numpy as np      # import library numpy dengan variabel np

citra1 = imread(fname="mobil.tif")
citra2 = imread(fname="boneka2.tif")

print('Shape citra 1 : ', citra1.shape)
print('Shape citra 1 : ', citra2.shape)

fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')
ax[0].set_title("Citra 1")
ax[1].imshow(citra2, cmap='gray')
ax[1].set_title("Citra 2")

# %proses filter median untuk citra mobil
# for baris=2 : tinggiA-1
#    for kolom=2 : lebarA-1
#        dataA = [inputMobil(baris-1, kolom-1) inputMobil(baris-1, kolom) inputMobil(baris-1, kolom+1)  ...
#              inputMobil(baris, kolom-1) inputMobil(baris, kolom) inputMobil(baris, kolom+1)  ...
#              inputMobil(baris+1, kolom-1) inputMobil(baris+1, kolom) inputMobil(baris+1, kolom+1)];
#        % Urutkan
#        for i=1 : 8
#            for j=i+1 : 9
#                if dataA(i) > dataA(j)
#                    tmpA = dataA(i);
#                    dataA(i) = dataA(j);
#                    dataA(j) = tmpA;
#                end
#            end
#        end
#        % Ambil nilai median
#        outputMobil(baris, kolom) = dataA(5);
#    end
# end

copyCitra1 = citra1.copy()
copyCitra2 = citra2.copy()

m1, n1 = copyCitra1.shape
output1 = np.empty([m1, n1])

m2, n2 = copyCitra2.shape
output2 = np.empty([m2, n2])
print('Shape copy citra 1 : ', copyCitra1.shape)
print('Shape output citra 1 : ', output1.shape)

print('m1 : ', m1)
print('n1 : ', n1)
print()

print('Shape copy citra 2 : ', copyCitra2.shape)
print('Shape output citra 3 : ', output2.shape)
print('m2 : ', m2)
print('n2 : ', n2)
print()

for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1],
                 copyCitra1[a1, b1-1], copyCitra1[a1,
                                                  b1], copyCitra1[a1, b1+1],
                 copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]]

        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output1[a1, b1] = dataA[5]

for baris in range(0, m2-1):
    for kolom in range(0, n2-1):
        a1 = baris
        b1 = kolom
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1],
                 copyCitra2[a1, b1-1], copyCitra2[a1,
                                                  b1], copyCitra2[a1, b1+1],
                 copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]]

        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output2[a1, b1] = dataA[5]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap='gray')
ax[1].set_title("Input Citra 1")

ax[2].imshow(output1, cmap='gray')
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2, cmap='gray')
ax[3].set_title("Output Citra 2")
plt.show()
# Import Library

# Load & Plot Input Image
# Membaca gambar dengan menggunakan imread dari skimage.io
citra1 = imread(fname="mobil.tif")
# Membaca gambar dengan menggunakan imread dari skimage.io
citra2 = imread(fname="boneka2.tif")

print('Shape citra 1 : ', citra1.shape)  # Menampilkan bentuk (shape) citra 1
print('Shape citra 2 : ', citra2.shape)  # Menampilkan bentuk (shape) citra 2

# Membuat subplot dengan 1 baris dan 2 kolom untuk menampilkan citra
fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()  # Melakukan unravel pada objek axes

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra 1 dalam skala abu-abu
ax[0].set_title("Citra 1")  # Memberikan judul pada citra 1
ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra 2 dalam skala abu-abu
ax[1].set_title("Citra 2")  # Memberikan judul pada citra 2

# Menyiapkan variable output
copyCitra1 = citra1.copy()  # Mengcopy citra 1 untuk mempersiapkan output
copyCitra2 = citra2.copy()  # Mengcopy citra 2 untuk mempersiapkan output

m1, n1 = copyCitra1.shape  # Mendapatkan ukuran baris dan kolom citra 1
# Membuat array kosong dengan ukuran yang sama dengan citra 1 untuk menyimpan hasil akhir
output1 = np.empty([m1, n1])

m2, n2 = copyCitra2.shape  # Mendapatkan ukuran baris dan kolom citra 2
# Membuat array kosong dengan ukuran yang sama dengan citra 2 untuk menyimpan hasil akhir
output2 = np.empty([m2, n2])

# Menampilkan bentuk (shape) copy citra 1
print('Shape copy citra 1 : ', copyCitra1.shape)
# Menampilkan bentuk (shape) output citra 1
print('Shape output citra 1 : ', output1.shape)

print('m1 : ', m1)  # Menampilkan nilai m1 (jumlah baris citra 1)
print('n1 : ', n1)  # Menampilkan nilai n1 (jumlah kolom citra 1)
print()

# Menampilkan bentuk (shape) copy citra 2
print('Shape copy citra 2 : ', copyCitra2.shape)
# Menampilkan bentuk (shape) output citra 2
print('Shape output citra 3 : ', output2.shape)
print('m2 : ', m2)  # Menampilkan nilai m2 (jumlah baris citra 2)
print('n2 : ', n2)  # Menampilkan nilai n2 (jumlah kolom citra 2)
print()

# Proses Filter Median Pada Citra Input 1
for baris in range(0, m1-1):  # Melakukan perulangan sebanyak jumlah baris citra 1
    for kolom in range(0, n1-1):  # Melakukan perulangan sebanyak jumlah kolom citra 1
        a1 = baris
        b1 = kolom
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1],
                 copyCitra1[a1, b1-1], copyCitra1[a1,
                                                  b1], copyCitra1[a1, b1+1],
                 copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]]

        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output1[a1, b1] = dataA[5]

# Proses Filter Median Pada Citra Input 2
for baris in range(0, m2-1):  # Melakukan perulangan sebanyak jumlah baris citra 2
    for kolom in range(0, n2-1):  # Melakukan perulangan sebanyak jumlah kolom citra 2
        a1 = baris
        b1 = kolom
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1],
                 copyCitra2[a1, b1-1], copyCitra2[a1,
                                                  b1], copyCitra2[a1, b1+1],
                 copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]]

        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output2[a1, b1] = dataA[5]

# Plot Citra Input dan Output Hasil dari Filter Rerata
# Membuat subplot dengan 2 baris dan 2 kolom untuk menampilkan citra input dan output
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()  # Melakukan unravel pada objek axes

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra 1 sebagai citra input
# Memberikan judul pada citra 1 sebagai citra input
ax[0].set_title("Input Citra 1")

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra 2 sebagai citra input
# Memberikan judul pada citra 2 sebagai citra input
ax[1].set_title("Input Citra 2")

# Menampilkan output hasil filter median dari citra 1
ax[2].imshow(output1, cmap='gray')
ax[2].set_title("Output Citra 1")  # Memberikan judul pada citra output 1

# Menampilkan output hasil filter median dari citra 2
ax[3].imshow(output2, cmap='gray')
ax[3].set_title("Output Citra 2")  # Memberikan judul pada citra output 2

plt.show()  # Menampilkan plot citra input dan output
