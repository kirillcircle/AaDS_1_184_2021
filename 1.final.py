print("TASK 1")
count = 0
ccount = 0
text = "The tiger once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin, and in the south from the foothills of the Himalayas to Bali in the Sunda islands."
for i in text:
    if i == 's':
        count += 1
    if i == 'a':
        ccount += 1
print(count)
print(ccount)

print("TASK 2")
from math import sqrt, pi
def calc(l):
    T = 2*pi*sqrt(l/9.8)
    print(round(T,2))
print("Введите длину математического маятника:")
calc(int(input()))

print("TASK 3")
print("1 is for +, 2 is for -, 3 is for *, 4 is for /, 5 is for **")
def Calculator(a,x,y):
    if a == 1:
        res = x + y
        print(res)
    elif a == 2:
        res = x - y
        print(res)
    elif a == 3:
        res = x * y
        print(res)
    elif a == 4:
        if y !=0:
            res = x / y
            print(res)
        else:
            print("y cannot be a zero")

    elif a == 5:
        res = x ** y
        print (res)
    else:
        print("sorry, you entered not correct number of operation")
a = int(input("Put the number of operation: "))
Calculator(a, int(input("X =" )), int(input("Y =" )))

print("TASK 4")
from math import *
def calc(p, m, n):
    return p*pow((1+(15/100/(m/12))), m/(12*n))
p = int(input("P ="))
m = int(input("m ="))
n = int(input("n ="))
print(calc(p, m, n))

print("TASK 5")
from math import *
def calc(k):
    mult = 1
    for n in range(k+1):
        mult = mult * ((n+pow(3, n))/(n+pow(5, 2*n)))
    print(mult)
calc(int(input("Введите k = ")))

print("TASK 6")
def Func(start, end):
    sum = 0
    numbers = list(range(start,end+1))
    for i in numbers:
        if i%2 == 1:
            sum+=i
    return  sum
x = int(input("От "))
y = int(input("До "))
print(Func(x, y))

print("TASK 7")
from math import sqrt
def calc(x,y,z):
    D = y**2 - 4*x*z
    if D > 0 and x!= 0:
        f1 = (-y + sqrt(D))/2*x
        f2 = (-y - sqrt(D))/2*x
        print(round(f1,2))
        print(round(f2,2))
    elif D == 0 and x!= 0:
        f1 = (-y)/2*x
        print(f1)
    elif D < 0:
        print("нет решений")
    else:
        print("ошибка")
print("Введите x, y, z")
calc(int(input()),int(input()),int(input()))

#TASK 8
number = int(input('Введите число: '))
if (number > 99999) and (number < 1000000):
    count = 0
    while(number > 0):
        count += number % 10
        number//= 10
    print(count)
else:
    print('error')