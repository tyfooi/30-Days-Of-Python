import random

age = 20
height = 5.8

base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))
area = .5*base*height
print("The area of the triangle is " + str(round(area)))

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a+side_b+side_c

print("The perimeter of the triangle is " + str(round(perimeter)))

# the next ones are literally the same as previous and a waste of time

if (len("python") != len("dragon")):
    print("this won't print")
    
if ("on" in ("python" and "dragon")):
    print("this will print")
    
sentence = "I hope this course is not full of jargon"
if ("on" in sentence):
    print("this also will print")
    
number = random.randint(0,10)
print("the number is" + str(number))
if number % 2 ==0:
    print("number is even")
else:
    print("number is odd")
    

# more random stuff not important, when will i use floor divison
# '' is a string and not a int so 19-20 are unimportant as well

weekly_hours_worked = int(input('Enter hours: '))
hourly_wage = int(input("Enter rate per hour: "))
wage = weekly_hours_worked * hourly_wage
print("Your weekly earning is $" + str(wage))


years_lived = int(input("enter number of years you have lived: "))
seconds_lived = 31,536,000 * years_lived
print("You have lived for ≈ " + str(seconds_lived) + "seconds")
cols = [1,2,3,4,5]
i = 1
for row in cols:
    print(i)
    print(" " + str(i/i))
    print(" " + str(i))
    print(" " + str(i*i))
    print(" " + str(i**i))
    i+=1
