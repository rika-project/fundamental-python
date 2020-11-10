print('tipe data skalar => tipe data sederhana')
anak1 = 'eko'
anak2 = 'dwi'
anak3 = 'tri'
anak4 = 'catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/array/daftar')
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Limo')
print(anak)

print('\nsapa anak ke-1')
print(f'Hai {anak[0]}!')

print('\nsapa semua anak')
for a in anak :
    print(f'Hai {a}!')

print('\nsapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}!')






