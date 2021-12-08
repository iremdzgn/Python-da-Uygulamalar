"""
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
"""   
# a = float(input('a: '))
    # result = ((a>0) and (a<100))
    # print(f'girilen sayı 0 ile 100 arasındadır: {result}')
"""
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
"""  
    # a = float(input('a: '))
    # result = (a > 0 and a % 2 == 0)
    # print(f'girilen sayı çift ve pozitiftir: {result}')

"""
3- Email ve Parola bilgileri ile giriş kontrolü yapınız
"""    
    # email = "email@iremduzgun.com"
    # password = "abc123"

    # girilenEmail = input('email: ')
    # girilenPassword = input('password: ')

    # result = (email==girilenEmail) and (password==girilenPassword)

    # print(f'giriş başarılı mı: {result}')

"""
4- Girilen 3 sayıyı büyüklük küçüklük olarak karşılaştırınız
"""    
    # a = float(input('a: '))
    # b = float(input('b: '))
    # c = float(input('c: '))

    # result= (a>b) and (a>c)
    # print(f'a en büyük sayıdır: {result}')

    # result= (b>a) and (b>c)
    # print(f'b en büyük sayıdır: {result}')

    # result= (c>b) and (c>a)
    # print(f'c en büyük sayıdır: {result}')


"""
5- Kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız
  Eğer ortalama 50 ve üstündeyse geçti Değilse Kaldı yazıdırın
  a)ortalama 50 olsa bile final notu en az 50 olmalıdır
  b)Finalden 70 alındığında ortalamanın önemi yoktur
"""
    # vize1 = float(input('1. vize: '))
    # vize2 = float(input('2. vize: '))
    # final = float(input('final: '))

    # ortalama = (((vize2+vize1)/2)*0.6) + (final*0.4)

    # result = ortalama >= 50
    # print(f'ortalamanız: {ortalama} ve öğrenci geçme durumu: {result}')

    # result = (ortalama>=50) and (final>=50)
    # print(f'ortalamanız: {ortalama} ve öğrenci geçme durumu: {result}')

    # result = (ortalama>=50) or (final>=70)
    # print(f'ortalamanız: {ortalama} ve öğrenci geçme durumu: {result}')

"""
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
  Formül: (Kilo/ boy uzunluğunun karesi)
  Aşağıdaki tabloya göre kişi hangi gruba girer
    0-18.4    => Zayıf
    18.5-24.9 => Normal
    25.0-29.9 => Fazla Kilolu
    30.0-34.9 => Şişman(Obez)
"""
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
