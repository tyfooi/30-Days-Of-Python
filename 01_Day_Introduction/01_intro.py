import math
# Exercise 1.2
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

# Exercise 1.3
print("tyfooi")
print("fooi")
print("United States")
print("I am enjoying 30 days of python")

# Exercise 1.4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh','Python','Finland']))
print(type("Your name"))
print(type("Your Country name"))
print(type("Your Country"))

# Exercise 3
# Euclidean formula sqrt((x2-x1)^2+(y2-y1)^2)

p1 = [2,3]
p2 = [10,8]

def find_distance_between_points(point1, point2):
    return (math.sqrt(((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2)))

print(find_distance_between_points(p1,p2))
    