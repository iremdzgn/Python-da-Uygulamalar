website = "http://www.iremduzgun.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?

result = len(course)
length = len(website)

# 2- 'website' içinden 'www' ifadesini alın.

result = website[7:10]

# 3- 'website' içinden 'com' karakterini alın.

result = website[22:25]
result = website[length-3:length]

# 4- 'course' içinden ilk 15 ve son 15 karakterini alın.

result = course[:15]
result = course[-15:]

# 5- 'course' içindeki ifadeleri tersten yazdırın.

result = course[::-1]

name, surname, age, job = 'Irem','Duzgun', 25, 'Ekonometrist'
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazırın.
# 'Benim Adım Irem Duzgun, Yaşım 25 ve Mesleğim Ekonometrist.'

result = f"Benim Adım {name} {surname}, Yaşım {age} ve Mesleğim {job}."
result = 'Benim Adım {} {}, Yaşım {} ve Mesleğim {}'.format(name,surname,age,job)

# 7- 'Hello world' ifadesindeki w karakterini W ile değiştirin.

say = 'Hello world'
result = say.replace('w','W')

# 8- 'abc' ifadesini yanyana 3 defa yazdırın.

alpha = 'abc'
result = alpha * 3


print(result)
