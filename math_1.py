import math #library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r
#lambda : .....

#contoh penggunaannya
jari_jari = 7
area = luas_lingkaran(jari_jari)
#area: ....
print (f"luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")