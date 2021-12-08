names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,2001,2002]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.

names.append('Cenk')
result = names

# 2- "Sena" değerinin listenin başına ekleyiniz

names.insert(0,'Sena')
result = names

# 3- "Deniz" ismini listeden siliniz.

# names.remove('Deniz')
# result = names

# 4- "Deniz" isminin indeksi nedir?

result = names.index('Deniz')

# 5- Ali listenin bir elemanı mıdır?

result = 'Ali' in names

# 6- Liste elemanlarını ters çevirin

result = names[::-1]

# 7- Liste elemanlarını alfabetik olarak sıralayın

names.sort()
# print(names)

# 8- Years listesini büyükten küçüğe doğru sırlayınız

years.reverse()
# print(years)

# 9- str = "Chevrolet,Dacia" karakter dizisini bir listeye çeviriniz
str = "Chevrolet,Dacia"
result = str.split(',')

# 10- Years dizisinin en küçük ve en büyük değerleri nelerdir

result = min(years)

# 11- years dizisinde kaç tane 1998 vardır

result = years.count(1998)

# 12- years dizisinin tüm elemanlarını siliniz

result = years.clear()

# 13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız

markalar =[]

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)



#print(result)
