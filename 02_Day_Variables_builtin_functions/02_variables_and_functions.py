# Level 1 Exercises
# 'Day 2: 30 Days of python programming'

first_name = "tyfooi"
last_name = "fooi"
full_name = "Mr.Tyfooi"
country = "United States"
city = "Nun-ya"
age = 25
year = 2024
is_married = False
is_true = True
is_light_on = False
part1, part2 = "I despise", "Single-line multi-define."

print(len(first_name))
print(max(len(first_name),len(last_name)))

num_one = 5
num_two = 4
total = num_one+num_two
diff = num_one-num_two
product = num_one*num_two
# this is tedious nty

circle_radius = 30
area_of_circle = 3.14*circle_radius**2
circum_of_circle = 2*3.14*circle_radius

user_input = input("What is the radius of your circle: ")
area_of_circle = 3.14*int(user_input)**2
print(area_of_circle)