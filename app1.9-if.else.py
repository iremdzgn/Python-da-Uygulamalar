import datetime

"""
1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
durumunu kontrol ediniz.ehliyet alma koşulu en az 18 yaş ve eğitim durumu 
lise yada üniversite olmalıdır.

"""
    # name = input('isim: ')
    # age = int(input('yaş: '))
    # edu = input('eğitim: ')

    # if (age >= 18) and (edu == 'lise' or edu == 'üniversite'):
    #     print(f'{name} adlı kişi ehliyet almaya hak kazanmıştır.')
    # else:
    #     print(f'{name} adlı kişi ehliyet alma hak kazanmamıştır.')
    

"""
2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
 not aralığına karşılık gelen not bilgisini yazdırınız
"""
#   0-24 => 0
#   25-44 => 1
#   45-54 => 2
#   55-69 => 3
#   70-84 => 4
#   85-100 => 5

    # yazili1 = float(input('1. yazılı notunuzu giriniz: '))
    # yazili2 = float(input('2. yazılı notunuzu giriniz: '))
    # sozlu = float(input('sozlu notunuzu giriniz: '))

    # ortalama = (yazili1+yazili2+sozlu)/3

    # if (ortalama >= 0) and (ortalama <= 24):
    #     print("öğrencinin notu 0'dır.")
    # elif (ortalama >= 25) and (ortalama <= 44):
    #     print("öğrencinin notu 1'dir.")
    # elif (ortalama >= 45) and (ortalama<= 54):
    #     print("öğrencinin notu 2'dir.")
    # elif (ortalama >= 55) and (ortalama<= 69):
    #     print("öğrencinin notu 3'tür.")
    # elif (ortalama >= 70) and (ortalama<= 84):
    #     print("öğrencinin notu 4'tür.")
    # else:
    #     print("öğrencinin notu 5'tir.")

"""
3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere 
göre hesaplayınız
"""
#   1. bakım => 1. yıl
#   2. bakım => 2. yıl
#   3. bakım => 3. yıl
#   **süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
#   ***datetime modülnü kullanmanız gerekiyor

tarih = input('aracınız hangi tarihte trafiğe çıktı(2019/8/9): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi -trafigeCikis
days = fark.days

if days <= 365:
    print('1. servis aralığı')
elif days > 365 and days <= 365*2:
    print('2. servis aralığı')
elif days > 365*2 and days <= 365*3:
    print('3. servis aralığı')
else:
    print('hatalı süre')
