name = input("What is your name?")
print("Hi " +name)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["Orange", "Banana", "Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"

def myfunc():
  print("Python is: " +x)
myfunc()

x = "awesome"

def myfunc():
  x = "fantatic"
  print("Python is: " +x)

myfunc()
print("Python is: " +x)

def myfunc():
  global x
  x = "fantatic"
myfunc()
print("Python is: " +x)

x = str(3)
y = int(3)
z = float(3)

x = 5
y = 'John'
print(type(x))
print(type(y))

birth_year = input("Enter your birth year: ")
age = 2023 - int(birth_year)
print(age)

x = int(input("Enter a value x = "))
if x < 0:
  print("It's negative")
elif x == 0:
  print("Equal to zero")
elif x < 5:
  print("Positive but smaller than or equal to 5")
else:
  print("Positive and lager than to 5")

for i in range(5):
  print(i)

sequence = [1, 2,None, 4, None, 5]
total = 0
for value in sequence:
  if value is None:
    continue
  total += value
print(total)

sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0
for value in sequence:
  if value == 5:
    break
  total_until_5 += value
print(total_until_5)

for i in range(4):
  for j in range(4):
    if(j > i):
      break
      print((i, j))

x = 256
total = 0
while x > 0:
  if total > 500:
    break
  total += x
  x = x // 2
print(x)

sum = 0
for i in range(101):
  sum += i
print(sum)

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

thislist = list(("apple", "banana", "cherry"))
print(thislist[1])
print(thislist[-1])
print(thislist[:2])
print(thislist[-3 : -1])

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for x in range(len(thislist)):
  print(thislist[x])

dict1 = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964,
    "colors" : ["read", "white", "blue"]
}
print(dict1)

def myfunc(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
myfunc(fruits)

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello is my name " +abc.name)

p1 = Person("John", 36)
p1.myfunc()
p1.age = 40
del p1.age

import numpy as np
data = np.random.randn(2,3)
data

import numpy as py
arr1 = np.arange(10)
arr1

import numpy as np
arr1[2:6] = 10
arr1

name = input("Your name is: ")
age = input("Age: ")
print("\nMy name is " +name)
print("\nAge = " +age)

def taxi():
  passengers = (int)(input("Nhap vao so nguoi: "))
  distance = (float)(input("Nhap vao so km: "))
  total = 2*passengers + 1.5*distance
  print("\nTotal: ", total)

taxi()

string = input("\nStrng enter: ")
print(string[::2])

sum = 0
n = 11
for i in range(n):
  if i%3 == 0 or i%5 == 0:
    sum += i
print(f"\nTong cac so tu 0 den {n} la boi cua 3 hoac 5 la: ", +sum)

a = [3, 9, 1, 4]
b = [2, 7, 4, 3, 8, 2]
min = len(b) if len(a) > len(b) else len(a)
c = a if len(a) > len(b) else b
for i in range(min):
  c[i] = a[i] + b[i]
print(c)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

import numpy as np
arr = np.array([41, 42, 43, 44])


filter_arr = []
for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

class Sach:
  dic_sach = {
      "masach": [],
      "tensach": [],
      "giaban": [],
      "soluong": []
  }

  def __init__(self, n):
    for i in range(n):
      ma = input("Nhap ma sach: ")
      ten = input("Nhap ten sach: ")
      dg = float(input("Nhap gia ban: "))
      sl = int(input("Nhap so luong: "))
      self.dic_sach['masach'].append(ma)
      self.dic_sach['tensach'].append(ten)
      self.dic_sach['giaban'].append(dg)
      self.dic_sach['soluong'].append(sl)

Sach(3)
print(Sach.dic_sach)
print("Tong so luong sach: " + str(sum(Sach.dic_sach["soluong"])))