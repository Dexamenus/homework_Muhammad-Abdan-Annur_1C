# DATA PRIBADI
print("1. DATA PRIBADI")
nama = (input('Masukan nama : '))
nik = int(input('Masukan NIK Anda : '))
tempat = str(input('Masukan Tempat Tinggal : '))
no = int(input('No HP : '))
print()

# Kelengkapan Syarat
print('2. KELENGKAPAN SYARAT')
wni = (input("input Kewargakenegaraan Anda : "))
pekerjaan = (input('Masukan Pekerjaan : '))
bpjs = (input('Keaktifan BPJS : '))
gaji = float(input('Masukan Gaji Anda : '))

# Syarat
daftar = ['asn','tni','polri']
js = ('aktif')
wei = ('indonesia')

if (wni in wei) and (pekerjaan not in daftar) and (bpjs in js) and (gaji <= 2000000):
    hasil = ('BERHAK MENDAPATKAN BANSOS')
else:
    hasil = ('TIDAK BERHAK MENDAPATKAN BANSOS')

print('-'*20)
print('Nama : ', nama)
print('NIK : ', nik)
print('Pekerjaan : ', pekerjaan)
print('Tempat Tinggal : ', tempat)
print('Nomor handphone : ', no)
print(hasil)

