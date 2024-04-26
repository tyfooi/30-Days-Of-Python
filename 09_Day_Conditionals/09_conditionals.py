import random
import traceback
import math

my_age = 25

try: 
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are old enough to drive.")
    else:
        print("You are not old enough to drive.")
        print("You need " + str(18-age) + " more years before you can drive.")
        
    if age > my_age:
        print("You are older than me.")
    elif age < my_age:
        print("You are younger than me.")
    else:
        print("You are my age!")
    
except:
    print("An input error occured")
    traceback.print_exc() 
    



try: 
    number_one = int(input("Enter number one: "))
    number_two = int(input("Enter number two: "))
    
    if (number_one < number_two):
        print(str(number_one) + " is greater than " + str(number_two))
    elif (number_one > number_two):
        print(str(number_one) + " is less than " + str(number_two))
    else:
        print(str(number_one) + " is equal to " + str(number_two))
        
except:
    print("An input error occured")
    traceback.print_exc() 
    

    
grades = {80:"A", 
          70:"B",
          60:"C",
          50:"D",
          0:"F"}

grade = random.randint(0,100)
print("The students grade = " + str(grade))
for key in grades:
    # print("The current key: " + str(key))
    if grade >= key:
        print("The student got an: " + str(grades.get(key)))
        break


months = {"autumn": ["september","october","november"],
          "spring": ["march", "april", "may"],
          "winter": ["december","january","february"],
          "summer": ["june", "july", "august"]}

try: 
    flag = False
    while(flag == False):
        while(True):
            month = input("Enter the current month: ").lower()
            if isinstance(month, str) != True:
                print('Please enter a string value. Example ("September")')
            else:
                break
                
        for key in months:
            for item in months.get(key):
                if item == month:
                    print("The current month is: " + str(key))
                    flag = True
                    break

        if flag == False:
            print("You did not enter an appropriate month")
except:
    print("An input error occured")
    traceback.print_exc() 
    

fruits = ['banana', 'orange', 'mango', 'lemon']

    
try:
    while(True):
        input_fruit = str(input("Enter a fruit: "))
        if input_fruit not in fruits:
            fruits.append(input_fruit)
            break
        else:
            print(str(input_fruit) + " is already in the list!")
    print("New fruit list: " + str(fruits))
except:
    print("An input error occured")
    traceback.print_exc() 
    
    
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    index = int((math.floor(len(person.get("skills"))/2)))
    if index % 2 == 0:
        print("Skills: " + str(person.get("skills")[index]) + ", " + str(person.get("skills")[index-1]))
    else:
        print(str((person.get("skills")[index])))
    
    if "Python" in person.get("skills"):
        print(person.get('first_name') + " " + person.get('last_name') + " knows Python!")
    else: 
        print(person.get('first_name')+ " " + person.get('last_name') + " doesn't know Python!")


# The other two are tedious and don't introduce new concepts