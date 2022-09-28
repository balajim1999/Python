###DAY - 2###

###FIRST PROGRAM

print('Hi i am balaji')
print("Hi i am balaji")
print('''Hi i am balaji''')

###GET INPUT FROM USER

name=input('What is your name = ')
age=int(input('What is your age = '))

print('My name is ',name,'I am ',age,'years old')

###ACCESSING THE INDEX FROM GIVEN STRING

name = 'Balaji'
print(name)
print(name[0])
print(name[-1])
print(name[2:5])
print(name[::2])

###ACCESSING THE INDEX FROM GIVEN STRING

name = 'muthuramalingam'
print(name)
print(name[2])
print(name[-7])
print(name[1:5])#slicing operator
print(name[-1:-5:-2])#step operator

###DAY - 3###

#Type casting
#float to int
price = 108.23      #float value
print(type(price))
change_price = int(price)  #int value
print(type(change_price))


#Type casting
#boolean to int

today_class = True      #boolean
print(type(today_class))
print(today_class)
change = int(today_class)
print(type(change))

#Type casting
#string to int

doorno = "1234" # string
change = int(doorno)
print(change)
print(type(change))

print(change)

#Type casting
#to float
price = 100
print(float(price))

print(float(False))
print(float(True))
print(float("20"))
print(float("20.5"))

#Operators
#Relational Operators
name1 = 'balaji'
name2 = 'ram'
print(name1 == name2)
print(name1 > name2)
print(name1 < name2)

#Relational Operators #Asky value
name1 = 'balaji'
name2 = 'Ram'
print(name1 == name2)
print(name1 > name2)
print(name1 < name2)

#Operator Chaining
no1, no2, no3 = 10, 15, 20
print(no1<no2<no3)
print(no1>no2>no3)
print(no1!=no2!=no3)
print(no1>no2<no3) 


#Arithmetic Operators
print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2//3)
print(20//3)#floor division
print(20/3)
print(20%3)
print(2**3) 

###DAY -4###

#Logical operators
#and or not
print(4 and 5)
print(4 or 5)
print(0 and 5)
print(0 or 5)
print(5 and 0)
print(5 or 0) 


#Bitwise operator
# & | ^ << >> ~

print(4 & 5)
print(4 | 5)
print(4 ^ 5) 
print(5 ^ 8)
no = 10
print(no)
print(~10) 

print(8<<1)

print(15<<2)

###DAY -5###

#Assignment Operators

#   += -= *= /= //= **= %= &= |= 

no = 10
no+=1
print(no)

no2 = 10
no2-=5
print(no2)

no3 = 15
no3*=5
print(no3)

no4 = 15
no4/=5
print(no4) 


# Ternary Operators

# Conditional Operator

no1, no2 = 10, 20

no3 = 30 if no1>no2 else 40

print(no3)

no1, no2 = 100, 20

no3 = 30 if no1>no2 else 40

print(no3) 

#Identity Operators

a = 10
b = 20
print(a is b)
print(a is not b)

#Identity Operators

a = 10
b = 10
print(a is b)
print(a is not b

#Membership Operators

#in, not in

st = 'Hi How are you?'
print('Hi' in st)
print('Hello' in st)

print('Hi' not in st)
print('Hello' not in st)

#eval function
#evaluation

result = eval(input(" Enter expression"))
print(result)

#string concatination

print("Hi"+"Hello")
print("Hi","Hello")

#String multiplication and addition

print("Hi"*3)#HiHiHi
print("Hi"+3)#TypeError

#Output sepration and end

a, b, c = 10, 20, 30
print(a, b, c, sep=" : ")
print(a, b, c, end=" : ")

#String formatting

print("Hi {0} Today is {1}".format("Muthu", "Monday")) 

#place holder or replacement operator

print("Hi {name} Today is {day}".format(name="Muthu", day = "Monday")) 

#place holder - Replacement Operator
name = 'Muthu'
day = "Monday"
print("Hi %s today is %s"%(name, day))

### DAY-6###
#Using if statement

mark = 90 #95   85
if mark>=95:
    print("Hi") 
else:
    print("Hello") 

mark = 95
if mark>=90:
    print("Hi") 
else:
    print("Hello")

#Using if statement

mark = int(input("Enter Mark: "))
if mark>=90:
    print("Hi")    
else:
    print("Hello") 

#Using if statement

mark1 = int(input("Enter Mark: "))
mark2 = int(input("Enter Mark: "))
if mark1>=90:
    if mark2>=90:
        print("Greater than 90 Both ")    
    else:
        print("Mark1 is greater than 90")
else:
    print("Mark1 is not greater than 90")

#Using if statement

mark1 = int(input("Enter Mark: "))
mark2 = int(input("Enter Mark: "))
if mark1>=90:
    if mark2>=90:
        print("Greater than 90 Both ")    
    else:
        print("Mark1 is greater than 90")
else:
    if mark2>=90:
        print("Mark2 is greater than 90")   
    print("Mark1, Mark2 is not greater than 90")

#Using if statement

name = input("Enter name: ")
if name == 'balaji':
    print('Welcome', name)
else:
    print("Welcome Guest")

#odd or even

no = 2 #Type Casting
if no%2 ==0:
    print('Even')
else:
    print("Odd") 

#odd or even

no = 3 #Type Casting
if no%2 ==0:
    print('Even')
else:
    print("Odd") 

#PRINT ODD AND EVEN NUMBERS

no = 1
while no<=20:
    if no%2 ==0:
        print(no, 'Even')
    else:
        print(no, "Odd")
    no+=1 

#PRINT EVEN NUMBERS ONLY

no = 1 
while no<=20:
    if no%2 ==0:
        print(no, 'Even')
   
    no+=1 

#PRINT ODD NUMBERS ONLY

no = 1 
while no<=20:
    if no%2 != 0:
        print(no, 'odd')
    no+=1 

#PRINT NUMBERS EXCEPT MULTUPLES OF 3

no = 1 
while no<=20:
    if no%3 != 0:
        print(no)
    no+=1

#PRINT MULTIPLES OF 3 AND 5

no = 1 
while no<=50:
    if no%3 == 0 and no%5 == 0 :
        print(no)
    no+=1 

### DAY- 7###

#GUESS THE CORRECT NUMBER GAME

import random

mind = random.randint(1,11)
print("Enter number between 1 and 10 ")

while True: 
    number = int(input("Enter number: "))

    if number == mind: 
        print("Yes, your guess is correct")
        break
    elif number>mind: 
        print("Your guess is greater")
    elif number<mind: 
        print("Your guess is smaller") 

#FLOWER GAME

temples = 7
flower = 1
while temples>=1:
	temples-=1 #6
	flower = flower + flower #2

print(flower) 

#DOSA GAME

balance = 8
count = 1
while count<=3: 
	eaten = balance/2
	balance = balance +eaten  #12
	count+=1
print(balance)

#EB BILL 

first_bill = int(input("1st two month EB bill = "))
secont_bill = int(input('2nd two month EB bill = '))
third_bill = int(input('3rd two month EB bill = '))
fourth_bill = int(input('4th two month EB bill = '))
fifth_bill = int(input('5th two month EB bill = '))
sixth_bill = int(input('6th two month EB bill = '))
income = int(input("monthly income= "))
total_bill = first_bill+secont_bill+third_bill+fourth_bill+fifth_bill+sixth_bill
average = total_bill/6
percent_permonth = ((average/income)*100)/2
print("EB bill per year",total_bill)
print("Average EB bill",average)
print("EB bill percentage from salary", percent_permonth)

#EB BILL

count=0
total_bill=0
while count<6:
    bill = input("do you have EB payment :")
    if bill=='yes':
        amount= int(input("enter the bill amount= "))
        count+=1
        total_bill+=amount
income = int(input("monthly income = "))
average = total_bill/count
percent_permonth = ((average/income)*100)/2
print(count)
print("EB bill per year",total_bill)
print("Average EB bill 2 month",average)
print("EB bill per month percentage from salary per month", percent_permonth)

#EB BILL

income = int(input("monthly income = "))
count=0
total_bill=0
while True:
    bill = input("do you have EB payment :")
    if bill=='yes':
        amount= int(input("enter the bill amount= "))
        count+=1
        total_bill+=amount
    elif bill=='no':
        break
average = total_bill/count
percent_permonth = ((average/income)*100)/2
print(count)
print("EB bill per year",total_bill)
print("Average EB bill 2 month",average)
print("EB bill per month percentage from salary per month", percent_permonth)

#PAPER COST

total_days          = int(input("Enter total days = "))
total_saturday      = int (input("Enter total saturday = "))
total_sunday        = int (input("Enter total sunday = "))
weekday_price       = int(input('Enter weekday paper price = '))
saturday_price      = int(input("Enter saturday paper price = "))
sunday_price        = int(input("Enter sunday paper price = "))
total_week_days          = total_days-(total_saturday + total_sunday)
saturday_price_total     = total_saturday * saturday_price
sunday_price_total       = total_sunday * sunday_price
weekday_price_total      = total_week_days * weekday_price
monthly_paper_price      = saturday_price_total + sunday_price_total + weekday_price_total
print(monthly_paper_price)

###DAY - 8###


