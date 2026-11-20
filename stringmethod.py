#ini repo untu latihan saja

nama = ('faisal').upper()#untuk mengubah semua huruf menjadi hutuf capital
print(nama)

nama2 = ('faisal').lower()#untuk mengubah semua huruf menjadi hutuf keil
print(nama2)


title = ('tenggelamnya kapal panderwik').title()#untuk mengubah setiap huruf depan kata menjadi huruf besar
print(title)

start = ('faizal pradana').startswith('faizal')
print(start)#untuk mengecek awalan kalimat

start = ('faizal pradana').endswith('pradana')
print(start)#untuk mengecek akhir kalimat

kota = 'makassar'.isalpha()
print(kota) #untuk mengcek huruf


kota = 'makassar'.isalnum()
print(kota) #untuk mengcek huruf dan angka

kota = 'makassar'.isspace()
print(kota) #untuk mengcek spasi, tab

nama3 = ['faisal','pradana']#
join = '_'.join(nama3)
print(join)

split = (join.split('_'))
print(split)

#sisah ljust dan rjust









