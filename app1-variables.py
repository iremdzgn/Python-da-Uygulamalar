"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşterinin adı
    Müşterinin soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
"""
musteriAdi = 'Irem'
musteriSoyad = 'Duzgun'
musteriAdSoyad = musteriAdi + ' ' + musteriSoyad
musteriCinsiyet = 'Kadın'
musteriTc = '39842842908490'
musteriDogumYili = 1995
musteriAdres = 'Ankara'
musteriYasi = 2020 - musteriDogumYili

"""
    Aşağıdaki sipariş bilgilerinin toplamlarını hesaplayınız.

    Sipariş 1 => 110 TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL
"""

order1 = 110
order2 = 1100.5
order3 = 356.95
toplam = order1 + order2 + order3
print("Toplam:", toplam)