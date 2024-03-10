#TASK2

#1
# list_price = [1,2,3,]
# a = len(list_price)
# b = 1
# for x in list_price:
#     b *= x
#     b += x
# print(b)  

#2
# sheet_list = [10,20,30,40,50]
# back = sheet_list[::-1]  
# print(back)

#3
# names_flowers = ['apple', 'pineapple', 'grapefruit']
# numbers_flowers = [1,25,33]
# name_number = zip(names_flowers,numbers_flowers)
# list_all = list(name_number)
# print(list_all)

#4
# number = [[1,2], [3,4], [6,7]]
# number.insert(2,5)
# print(number)
        
#5
# list_price = ['toyota supra', 'nissan gtr ', 'maclaren']
# list_price.insert(1,'vaz2107')
# print(list_price)

#6
# print(' Verilmis listin ededi ortasini tapin')
# number = [2,4,5,6]
# average = sum(number)/len(number)
# print('Aferin:', average)

#7
# numers = input()
# even = 1
# odd = 20
# for x in numers:
#     if int(x) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print('Even: %od, odd: %d' % (even,odd))       
    

#8
# fruits = ['banan', 'apple', 'cherry', 'banan', 'cherry']
# print(set(fruits))

#9
# a = ['Fuad', 'Rovsen', 'Orxan']

# choise = input(" (1) Elave et (2) Sil :")

# if choise == '1':
#     name = input("Ad Daxil edin : ")
#     if name == '':
#         print(" Zehmet olmasa Ad Daxil edin")
#     elif len(name) > 15:
#         print("Maksimum 15 daxil edin  ")
#     else:
#         a.append(name)
#         print(a)
# if choise == '2':
#     ad = input("Silmek istediyiniz adi daxil edin : ")
#     if ad == '':
#         print(" Ad daxil etmediniz")
#     elif ad not in a:
#         print("Bu ad bazada yoxdur")
#     else :
#         a.remove(name)

#10
# virtual_printer = ('Java')
# print(6*'Java\n')