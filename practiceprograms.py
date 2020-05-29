"""
#Exercise 1-Hello
name = input("What is your name")
print('hello', name)
"""

"""
#Exercise 2- Area of a room
width = float(input('What is the width of your room'))
length = float(input('What is its length'))
print('The area of your room is :', str(width * length) , 'fts')
"""

"""
#Exercise 3- Area of a field
width = float(input('What is the width of your farm in fts'))
length = float(input('What is its length in fts'))
area = (width * length) / 43560
print('The area of your field is :' , str(area) , 'acres' )
"""

"""
#Exercise 4 - Bottle Deposits
size_of_bottle = float(input('What is the size of your bottle: '))
number_of_bottles = int(input('How many bottles are you depositing: '))

if size_of_bottle < 1:
    print("your refund is: " , str(size_of_bottle * number_of_bottles * 0.10))
elif size_of_bottle > 1:
    print('Your refund is: ' , str(size_of_bottle * number_of_bottles * 0.25))
"""
"""
# Exercise 5 - Tax and Tip
customer = float(input('What is the cost of your meal '))
local_tax = customer * 0.2
tip = customer - local_tax
real_tip = tip * 0.18
grand_total = customer + local_tax + real_tip

print("Your voucher reads as follows: ",
      "Total amount: ", str(grand_total), "Local Tax: ", str(local_tax),
      "Tip: ", str(real_tip)
      )
"""
"""
#Exercise 6- Sum of first n positive integers
#takes input from user
n = int(input('Enter any integer: '))
#sets argument
for n in range(1, n):
    print(str(n * n + 1 / 2))
n = n + 1
"""

"""
#Exercise 7 - Heights Units
height_in_fts = int(input('What is your height in feets'))
height_in_inches = int(input('what is your height in inches'))
fts_in_cm = 12 * 2.54 * height_in_fts
inches_to_cm = 2.54 * height_in_inches
print('Your heights in centimetres is: ', fts_in_cm + inches_to_cm)
"""
"""
#Exercise 8 - Even or odd
magic_number = int(input('Enter a number of your choice'))
if magic_number % 2 == 1:
    print('Your number is odd')
else:
    print('Your number is even')
"""
"""
#Exercise 9 - Assessing employees
Unacceptable = 0.0
Acceptable = 0.4
Meritorius = 0.6

workers_rate = float(input('Enter your years rate'))
if workers_rate == Unacceptable:
    performance = "Unacceptable"
elif workers_rate == Acceptable:
    performance = 'Acceptable'
elif workers_rate >= Meritorius:
    performance = 'Meritorius'
else:
    performance = ""

if performance == "":
    print('you entered a wrong input')
else:
    print('Based on that raise the performance is %s' %performance)
    print('Your raise therefore is %s' %(workers_rate * 2400))
"""
"""
#Exercise 10- Is it a leap year?
year = int(input('Enter a year: '))
if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

if leap_year:
    print('Yes its a leap year')
else:
    print('No its  not a leap year')
"""
""""
#Exercise 11 - Roulette Payout
#import spinwheel
from random import randrange
pay = randrange(0, 38)
#showing result of spin
if pay == 37:
    print('Your spin is 00')
else:
    print('Your spin is' ,pay)
#check the color of card
if pay % 2 == 1 and pay >= 1 and pay <=9 or\
    pay % 2 == 0 and pay >= 12 and pay <= 18 or\
    pay % 2 == 1 and pay >= 19 and pay <= 27 or\
    pay % 2 == 0 and pay >=30 and pay <= 36:
    print('The pay is red')
elif pay == 00 and 37:
    print('Pay is green')
else:
    print('The pay is black')
#Check odd or even
if pay % 2 == 0:
    print('Your pay is even')
else:
    print('Your pay is odd')
#Check number group
if pay >=1 and pay <= 18:
    print('Your pay falls between 1 and 18')
elif pay == 37:
    pass
else:
    print('Your pay falls between 19 and 36')
"""
"""
#Exercise 11 - Average
 # This program calculates the average of a series
# of numbers entered by the user.

# Explain what we are doing.
print('This program calculates the average of')
print('numbers you will enter.')
#this is the accumulator variable
total = 0.0
dividend = 0
series = int(input('Enter the number, otherwise press 0 to end : '))
# Get the numbers and accumulate them.
while series != 0:
    total += series
    dividend += 1
    # could also be written as total += number
    series = int(input('Enter the  number, otherwise press 0 to end: '))
#could also be written as total += number
print(total)
print(dividend)
# Display the average of the numbers.
average = total / dividend
print(average)
"""
""""
#Exercise 12- Discounts
#Displays heading of table
print('OldPrice \t Discount \t NewPrice')
print('------------------------------')
#formula for discount
old_price = [4.95, 9.95, 14.95, 19.95, 24.95]
discount_rate = 0.60
for price in old_price:
    Discount = (price * discount_rate)
    New_Price = (price - Discount)
    print(price, '\t', '\t', format( Discount, '.2f'), '\t', '\t', format(New_Price, '.2f'))
 """
"""
#Exercise 13 - Temperature Conversion Table
#TableHead
print('0C \t \t 0F')
print('------------')
for degree_celcius in range(0,110,10):
    degree_fahrenheit = degree_celcius * 1.8 + 32
    print(degree_celcius, '\t', '\t', degree_fahrenheit)
"""
#Exercise 14- Admission Price
#set argument
guest = int(input('Enter the age of all users or blank to quit: '))
total = 0.0
for x in guest:
    if x <= 2:
        cost = 0.00
    elif 3 <= x <= 12:
        cost = 14.00
    elif x >= 65:
        cost = 18.00
    else:
        cost = 23.00
    guest = int(input('Enter the age of all users or blank to quit: '))
    total += cost
    print(total)



while guest != "":
    guest = int(input('Enter the age of all users or blank to quit: '))
    total += cost
    guest = int(input('Enter the age of all users or blank to quit: '))
    print(total)













