sayilar = [1,3,5,7,9,12,19,21]

''''
1- Sayılar dizisini while ile ekrana yazdırın
'''

# i = 0
# while (i< len(sayilar)):
#     print(sayilar[i])
#     i+=1

'''2- Başlangıç ve bitiş değerlerinin kullancıdan alıp aradaki tüm tek sayıları 
  ekrana yazdırın
'''
# start = int(input('başlangıç sayısını giriniz: '))
# end = int(input('bitiş sayısını giriniz: '))

# i=start
# while (i < end):
#     i += 1
#     if i % 2 == 1:
#         print(i)


'''
3- 1-100 arasındaki sayıları azalan şekilde yazdırın

'''
# i = 100
# while i>0:
#     print(i)
#     i -= 1

'''
4- Kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın

'''
# numbers = []
# i = 0
# while i <5:
#     sayi = int(input('sayı: '))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print(numbers)

'''
5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde 
saklayınız
  **ürün sayısını kullanıcıya sorun
  **dictionary listesi yapısı (name,price )şeklinde olsun
  **ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyiniz

'''
# urunler = []

# adet = int(input('ürün sayısını giriniz: ')

# i = 0

# while (adet > i):
#     name = input('ürün adı: ')
#     price = input('ürün fiyatı: ')
#     urunler.append({
#         'name': name,
#         'price': price
#     })
#     i += 1

# for urun in urunler:
#     print(f'ürün adı: {urun['name']} ve ürün fiyatı: {urun['price']}')