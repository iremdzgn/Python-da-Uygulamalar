x, y, z = 2, 5, 107

numbers = 1,5,7,10,6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
    # sayı1 = int(input('1. sayıyı giriniz: '))
    # sayı2 = int(input('2. sayıyı giriniz: '))
    # çarpım = sayı1*sayı2
    # toplam = x + y + z
    # result = çarpım - toplam83

# 2- y'ni x'e kalansız bölümünü hesaplayınız.
result = y//x

# 3- (x,y,z) toplamının mod 3'ü nedir?
result = (x+y+z)%3
# 4- y'nin x. kuvvetini hesaplayınız
result=y**x
# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır?
x, *y, z = numbers
result = z**3
# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
x, *y, z = numbers
result = sum(y)

print(result)