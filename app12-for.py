sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesindeki hangi sayılar 3'ün katıdır?

# for num in sayilar:
#     if (num % 3 == 0):
#         print(num)

# 2- Sayılar listesindeki sayıların toplamı kaçtır?

# toplam = 0
# for num in sayilar:
#     toplam += num
# print(f'toplam: {toplam}')

# 3- Sayılar listesindeki tek sayıların karesini alınız.

# for num in sayilar:
#     if (num % 2 == 1):
#         print(num **2 )

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?

# for i in sehirler:
#     if len(i) <= 5:
#       print(i)

urunler = [
    {'name': 'samsung S6','price':3000},
    {'name': 'samsung S7', 'price':4000},
    {'name': 'samsung S8', 'price': 5000},
    {'name': 'samsung S9', 'price': 6000},
    {'name': 'samsung S10', 'price': 7000}
]

# 5- Ürünlerin fiyatları toplamı nedir?
# toplam = 0
# for urun in urunler:
#     toplam += urun['price']
# print(toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz

for i in urunler:
    if i['price'] <= 5000:
        print(i)
