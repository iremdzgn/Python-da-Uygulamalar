# 1- "Bmw, Opel, Mazda, Mercedes" elemanlarına sahip bir liste oluşturunuz.

cars = ["Bmw","Opel","Mazda","Mercedes"]
#print(cars)

# 2- Listede kaç eleman vardır?
result = len(cars)

# 3- Listenin ilk ve son elemanı nedir ?

result = cars[1]
result = cars[-1]

# 4- Mazda değrini Toyota ile değiştirin

#cars[2] = 'Toyota'
result = cars

# 5- Mercedes listenin bil elemanı mıdır ?

result = 'Mercedes' in cars

# 6- Listenin -2 değeri nedir?

result = cars[-2]

# 7- Listenin ilk 3 elemanını alın

result = cars[:3]

# 8- listenin son iki elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.

cars[-2:] = ['Toyota','Renault']
result = cars

# 9- Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin

result = cars + ['Audi','Nissan']

# 10- Listenin son elemanını siliniz.

del cars[-1]
result = cars

# 11- Liste elemanlarını tersten yazdırın.

result = cars[::-1]

# 12- Aşağıdaki bilgileri bir liste içersinde saklayınız

    # studentA: Irem Duzgun, 1995, (70,40,60)
    # studentB: Sena Duzgun, 1997, (89,90,60)
    # studentC: Selma Duzgun, 1975, (60,70,90)
    # studentD: Ismail Duzgun, 1966, (70,80,80)

studentA = ['Irem','Duzgun',1995, [70,40,60]]
studentB = ['Sena', 'Duzgun', 1997, [89,90,60]]
studentC = ['Selma', 'Duzgun', 1975, [60,70,90]]
studentD = ['Ismail', 'Duzgun', 1966, [70,80,80]]

# 13- Liste elemanlarını yazdırınız

result = studentA[0]
result = studentB[1]
result = studentC[2]
result = studentD[3]

result = f"{studentA[0]} {studentA[1]} {2020-studentA[2]} yaşında ve not ortalaması {int((studentA[3][0] + studentA[3][1] + studentA[3][2])/3)} "


print(result)
