website = "http://www.iremduzgun.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- ' Hello World ' yazı dizisindeki baştaki ve sondaki boşlukları siliniz.t

s = ' Hello World '
result = s.strip()

# 2- 'www.sadikturan.com' ifadesi içersindeki sadikturan bilgisi haricindeki tüm bilgileri silin.

result = 'www.iremduzgun.com'.strip('w.com')

# 3- 'course' içersindeki tüm karakterleri küçük harf yapın.

result = course.lower()

# 4- 'website' içersinde kaç tane 'a ' harfi vardır?

result = website.count('a')

# 5- 'website' www ile başlayıp com ile bitiyor mu?

result = website.startswith('www')
result = website.endswith('com')

# 6- 'website' içersin .com ifadesi var mı?

result = website.find('.com')
result = website.find('.com',0,10)

# 7- 'course ' ifadesi içersindeki karakterlerin hepsi alfabetik mi?

result = course.isalpha()
result = course.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içersine terleştiri sağ ve soluna * koyunuz.

result = 'Contents'.center(50,'*')

# 9- 'course' ifadesindeki tüm boşluk karakterlerini '-' ile değiştiriniz.

result = course.replace(' ','-')

# 10- 'Hello World ' ifadesindeki World ifadesini There ile değiştirin.

s = 'Hello World'
result = s.replace('World','There')

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

result = course.split()





print(result)
