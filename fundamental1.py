# konstruksi dasar python
# sequential : ekseskusi berurutan
print('Hello World!')
print('Rika Sahriana')
print('Tanggal 10 November 2020')
print('-' * 50)

#percabangan: eksekusi terpilih
ingin_cepat = False
if ingin_cepat :
    print('jalan lurus aja bos!')
else :
    print('muter aja bos!')

#Percabangan lebih dari 2
ingin_balik = True

#Perluangan
jumlah_anak = 4
for index_anak in range(1, jumlah_anak+1): #jumlah anak = 5 - 1 = 4
    print(f'hallo anak {index_anak}')
