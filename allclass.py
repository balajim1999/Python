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

