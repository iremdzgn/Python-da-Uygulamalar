# 1- Girilen 2 sayıdan hangisi büyüktür?
    # a = int(input('a: '))
    # b = int(input('b: '))
    # result = (a > b)
    # print(f"a: {a} b: {b} den büyüktür: {result}")

# 2- Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
    # vize1 = float(input('1. vize: '))
    # vize2 = float(input('2. vize: '))
    # final = float(input('final: '))
    # ortalama = ((((vize1 + vize2)/2) * 0.6) + (final * 0.4))

    # print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın
    # a = int(input('bir sayı giriniz: '))
    # result = a % 2 == 0
    # print(result)
# 4- Girilen bir sayının negatif pozitif durumunu yazdırın
    # b = float(input('bir sayı giriniz: '))
    # result = b < 0
    # print(f'girilen sayı negatiftir: {result}')
# 5- parola ve Email bilgisini isteyip doğruluğunu kontrol ediniz
#   (email: email@iremduzgun.com parola:abc123)

email = 'email@iremduzgun.com' 
password = 'abc123'

girilenEmail = input('email giriniz: ')
girilenPassword = input('password giriniz: ')

isEmail = (email == girilenEmail)
isPassword = (password == girilenPassword)

print(f'girilen email bilgisi doğrudur: {isEmail} ve girilen password doğrudur: {isPassword}')

#print(result)
