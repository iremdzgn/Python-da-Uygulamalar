#Bankamatik Uygulaması

iremHesap ={
    'ad':'İrem Düzgün',
    'hesapNo':'1234567',
    'bakiye':3000,
    'ekHesap':2000
}

senaHesap ={
    'ad':'Sena Düzgün',
    'hesapNo':'1234234',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap ['bakiye'] = hesap['bakiye'] - miktar
        print('paranızı alabilirsiniz..')
        bakiyeSorgula(hesap)
    else:
        toplam = int(hesap['bakiye']) + int(hesap['ekHesap'])

        if (toplam >= miktar):
            ekHesapKullanımı = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanımı == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar

                print('paranızı alabilirsiniz..')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır")
        else:
            print('üzgünüz bakiye yetersiz')

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz: {hesap['ekHesap']} TL'dir.")

paraCek(iremHesap,3000)
print('*******************')
paraCek(iremHesap,2000)
