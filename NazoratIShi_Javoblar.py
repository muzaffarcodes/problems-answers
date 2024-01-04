# 1
"""
son1 = int(input("Son1: "))
son2 = int(input("Son2: "))
num1,num2 = son2,son1
print("Son1: ",num1)
print("Son2: ",num2)

# 2

num = int(input("Son kiriting: "))
son = str(num)
print("Teskarisi: ",son[::-1])

# 3

soz = input("So'z kiriting: ")
word = str(soz)
print("Teskarisi: ",word[::-1])

# 4

list1 = [23,4,54,465,786,23,343222,421.3,4354,707]
print(list1[::-1])

# 5

list2 = [1,2,3,4,5,6,7,8,1,2,3,4,5]
print(list2.count(3))

# 6

my_list = [1,2,3,4,5,6,7,8,9,0,10,11,12]
even_numbers = list(filter(lambda x: x % 2 == 0,my_list))
print("Juftlar: ",even_numbers)

my_list1 = [1,2,3,4,5,6,7,8,9,0,10,11,12]
odd_Numbers = list(filter(lambda x: x % 2 == 1,my_list1))
print("Toqlar: ",odd_Numbers)

# 7

son1 = float(input("Son1: "))
son2 = float(input("Son2: "))

natija = abs(son1) - (-(abs(son2)))
print(natija)

# 8

for i in range(3):
	for j in range(3):
		print(j*i * "*")

# 9

fb = [0,1,1,]
x = 1
y = 1

for i in range(10):
    z = x + y
    x = y
    y = z
    fb.append(z)

faylnomi = "fibonaci.txt"
with open(faylnomi, "w") as fayl:
    fayl.write(f"{fb}")
    
n = int(input("n-fibonachi sonini toping:"))
print("{} - fibonachi soni =  {}".format(n,fb[n-1] + fb[n-2]))

print("")
a = 0
for i in fb:
    print(f"{a}-son: {i}")
    a += 1

print("{} - fibonachi soni =  {}".format(n,fb[n-1] + fb[n-2]))

# 10
import random

list1 = [[],[],[],]
for i in range(3):
	for j in range(3):
		list1[i].append(random.randint(1,9))
print("Matrix: \n")
for i in list1:
	print(i)

start = list1[0][0] + list1[1][1] + list1[2][2]
stop = list1[2][0] + list1[1][1] + list1[0][2]
abs_qiymat = abs(start-stop)
print(f"Absolyut qiymat: {start} - {stop} = {abs_qiymat}")

# 11

# 1 - usul
l1 = [32,43,12,23,3,68,74,34,10,0,1,-1,2]
l1.sort()
print("O'sish tartibida sortlash: ",l1)

# 2 - usul
l2 = [0,-1,-16,23,45,31,19,20,22,39]
print("O'sish tartibida sortlash: ",sorted(l2))

# 3 - usul
l3 = [3,4,21,0,0,2,32,41,31,33,54,27]
l3.sort(reverse=False)
print("O'sish tartibida sortlash: ",l3)

# 12

def readByNumber(enteredNum):
    dict1 = {1:"o'n",2:"yigirma",3:"o'ttiz",4:"qirq",5:"ellik",6:"oltmish",7:"yetmish",8:"sakson",9:"to'qson"}
    dict2 = {1:"bir",2:"ikki",3:"uch",4:"tort",5:"besh",6:"olti",7:"yetti",8:"sakkiz",9:"to'qqiz"}
    num = enteredNum//10
    num2 = enteredNum % 10
    print(dict1[num],end=(" "))
    print(dict2[num2])    
readByNumber(int(input("Enter number to read: "))) 

# 13
b = 0
a = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
listb = [x for i in a for x in i]

for i in listb:
    b += i
    
print(b)

# 14

sozlar = ['Salom','Hayr','Assalom','Sariq','Pult']
list1 = [a for a in sozlar if 'a' in a]
print(*list1,sep = ' - ')

# 15

print("List kiriting: ")
yangi_list = []
i = 1
while i <= 10:
	try:
		num = float(input(f"{i} - son: "))
		yangi_list.append(num)
		i += 1
	except:
		print("Son kiritng!!!")

print("Elementlar: ",*yangi_list)

# 16

son = input("Son kiriting: ")
if son[0] == son[-1]:
	print("Son palindrome!")
else:
	print("Son palindrome emas!")

# 17

soz = input("So'z kiriting: ")
if soz[0] == soz[-1]:
	print("So'z palindrome!")
else:
	print("So'z palindrome emas!")

# 18

lst = [
       [
        [1,2,3],
        [4,5,6]
       ],
       [
        [7,8,9],
        [1,2,3]
       ],
       [
        [1,2,3],
        [1,2,3]
       ]
      ]


newList = [print(c,end = " ") for a in lst  for b in a  for c in b]

# 19 
# ...?

# 20

a = [2,3,4,2,4,5,1]
a.sort()
print("O'rtadagi Sortlangan son: ",a[len(a)//2])

# 21,22,23,24 boshqa fayllarda.

"""