import random
import string

karakter = ' ' + string.ascii_letters + string.punctuation + string.digits
karakter = list(karakter)
kunci = karakter.copy()
random.shuffle(kunci)

print(karakter)
print(kunci)

yang_ingin_diubah = input('masukkan teksnya: ')
kode = ''
jawaban = ''

for huruf in yang_ingin_diubah:
    index = karakter.index(huruf)
    kode += kunci[index]

print(kode)

yang_ingin_dipecahkan = input('masukkan kode yang ingin dipecahkan: ')
for huruf in yang_ingin_dipecahkan:
    index = kunci.index(huruf)
    jawaban += karakter[index]

print(jawaban)






