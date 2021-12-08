ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler[number] = {
    'ad':name,
    'soyad':surname,
    'telefon':phone
}

ogrenciler.update({
    number: {
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")


ogrenciler.update({
    number: {
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})

print(ogrenciler)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[number]
print(ogrenci)
