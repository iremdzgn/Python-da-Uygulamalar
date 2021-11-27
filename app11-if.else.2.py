"""
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
a = float(input('a: '))
result = ((a>0) and (a<100))
print(f'girilen sayı 0 ile 100 arasındadır: {result}')
"""
# a = float(input('a: '))
# result = ((a>0) and (a<100))

# if result :
#     print('girilen sayı 0 ile 100 arasındadır.')
# else:
#     print('girilen sayı 0 ile 100 arasında değildir.')


"""
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
a = float(input('a: '))
result = (a > 0 and a % 2 == 0)
print(f'girilen sayı çift ve pozitiftir: {result}')
"""
# a = float(input('a: '))
# result = (a > 0 and a % 2 == 0)

# if result:
#     print('girilen sayı pozitif bir çift sayıdır.')
# else:
#     print('girilen sayı ppozitif bir çift sayı değildir.')

"""
3- Email ve Parola bilgileri ile giriş kontrolü yapınız
email = "email@iremduzgun.com"
password = "abc123"

girilenEmail = input('email: ')
girilenPassword = input('password: ')

result = (email==girilenEmail) and (password==girilenPassword)

print(f'giriş başarılı mı: {result}')
"""

# email = "email@iremduzgun.com"
# password = "abc123"

# girilenEmail = input('email: ')
# girilenPassword = input('password: ')

# if email == girilenEmail:
#     if password == girilenPassword:
#         print('giriş başarılı..')
#     else:
#         print('lütfen geçerli bir parola giriniz..')
# else:
#     print('lütfen email adresinizi doğru giriniz..')
    

"""
4- Girilen 3 sayıyı büyüklük küçüklük olarak karşılaştırınız
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    result= (a>b) and (a>c)
    print(f'a en büyük sayıdır: {result}')

    result= (b>a) and (b>c)
    print(f'b en büyük sayıdır: {result}')

    result= (c>b) and (c>a)
    print(f'c en büyük sayıdır: {result}')
"""
# a = float(input('a: '))
# b = float(input('b: '))
# c = float(input('c: '))

# if a>b:
#     if a>c:
#         print('a en büyük sayıdır')
#     else:
#         print('c en büyük sayıdır')
# elif b>a :
#     if b>c:
#         print('b en büyük sayıdır')
#     else:
#         print('c en büyük sayıdır')
# elif c>a and c>b:
#     print('c en büyük sayıdır')

"""
5- Kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız
  Eğer ortalama 50 ve üstündeyse geçti Değilse Kaldı yazıdırın
  a)ortalama 50 olsa bile final notu en az 50 olmalıdır
  b)Finalden 70 alındığında ortalamanın önemi yoktur

    vize1 = float(input('1. vize: '))
    vize2 = float(input('2. vize: '))
    final = float(input('final: '))

    ortalama = (((vize2+vize1)/2)*0.6) + (final*0.4)

    result = ortalama >= 50
    print(f'ortalamanız: {ortalama} ve öğrenci geçme durumu: {result}')

    result = (ortalama>=50) and (final>=50)
    print(f'ortalamanız: {ortalama} ve öğrenci geçme durumu: {result}')

    result = (ortalama>=50) or (final>=70)
    print(f'ortalamanız: {ortalama} ve öğrenci geçme durumu: {result}')
"""
# dslşak
# #Durum 1
# if ortalama >=50:
#     if(final >= 50):
#         print(f"öğrencinin ortalaması {ortalama} ve geçme durumu: Başarılı..")
#     else:
#         print(f"öğrencinin ortalaması {ortalama} ve geçme durumu: Başarısız.. Finalden en az 50 almalısınız.")
# else:
#     print(f"öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarısız")    

# Durum2
# if ortalama >= 50:
#      print(f"öğrencinin ortalaması {ortalama} ve geçme durumu: Başarılı..")
# else:
#     if final >= 70:
#         print(f"öğrencinin ortalaması {ortalama} ve geçme durumu: Finalden 70 ve üzeri aldığı için Başarılı..")
#     else:
#         print(f"öğrencinin ortalaması: {ortalama} ve geçme durumu: Başarısız")    


    

"""

6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
  Formül: (Kilo/ boy uzunluğunun karesi)
  Aşağıdaki tabloya göre kişi hangi gruba girer
    0-18.4    => Zayıf
    18.5-24.9 => Normal
    25.0-29.9 => Fazla Kilolu
    30.0-34.9 => Şişman(Obez)

name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg)/(hg**2)

zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
fazlaKilolu = (index > 24.9) and (index <= 29.9)
sisman = (index > 29.9) and (index < 34.9)

print(f'{name} boy kile indexin { index} ve index değerlendirmen zayıf: {zayif}')
print(f'{name} boy kile indexin { index} ve index değerlendirmen normal: {normal}')
print(f'{name} boy kile indexin { index} ve index değerlendirmen fazla kilolu: {fazlaKilolu}')
print(f'{name} boy kile indexin { index} ve index değerlendirmen şişman{sisman}')

"""

name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg)/(hg**2)

if (index >= 0) and (index <= 18.4):
  print(f'{name} boy kile indexin { index} ve index değerlendirmen: Zayıf')
elif (index > 18.4) and (index <= 24.9):
  print(f'{name} boy kile indexin { index} ve index değerlendirmen: Normal')
elif (index > 24.9) and (index <= 29.9):
  print(f'{name} boy kile indexin { index} ve index değerlendirmen: Fazla Kilolu')
else:
  print(f'{name} boy kile indexin { index} ve index değerlendirmen: Şişman')






