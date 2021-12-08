'''
1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız

'''
# def yazdır(kelime, adet):
#     print(kelime*adet)
# yazdır('Merhaba\n',10)

'''
2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız

'''
# def listeyeCevir(*params):
#     liste =[]

#     for i in params:
#         liste.append(i)

#     return liste

# result = listeyeCevir(10,30,'Irem','Merhaba',40)
# print(result)

'''
3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun

'''
# def asalSayilariBul(sayi1,sayi2):
#     for sayi in range(sayi1,(sayi2+1)):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if sayi % i ==0:
#                     break
#             else:
#                     print(sayi)

# sayi1 = int(input('sayı 1: '))
# sayi2 = int(input('sayı 2: '))

# asalSayilariBul(sayi1,sayi2)


'''
4- Kendine gönderilen bir sayının tam bölenlerinni bir liste şeklinde döndürün

'''
def tamBolenBul(sayi):
    tamBolenler = []

    for i in range(2 , sayi):
        if ( sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenBul(30))
