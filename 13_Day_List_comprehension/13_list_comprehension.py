import random

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

def negative_and_zero(l):
    return [i for i in range(len(l)-1) if i % 2 == 0 or i == 0]

print(negative_and_zero(numbers))

def flatten(l): # He definitely overcomplicated this but I understand now
    return [elements for sublist in l for item in sublist for elements in item]

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print(flatten(list_of_lists))


def create_tuples():
    return [(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]

print(create_tuples())

# bro 4 is just an easier 2



def list_to_dict(l): # bro actually stop making sub sub lists
    return {subsublist[0]: subsublist[1] for sublist in l for subsublist in sublist}
    
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print(list_to_dict(countries))


def list_of_sublists_to_string(l):
    return [(' '.join(x)) for sublist in l for x in sublist]

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

print(list_of_sublists_to_string(names))

slope = lambda m,x,b : m*x+b

print(slope(random.randint(0,8),random.randint(0,8),random.randint(0,8)))