from countries import countries
from countries_data import data

for i in range(10):
    print(i)
    
n = 0
while(n<10):
    n+=1
    print(i)
    
    
output = ""
for i in range(7):
    output += "#"
    print(output)
    
hashes = ["#", "#", "#", "#", "#", "#", "#", "#"] 
for i in range(8):
    for item in hashes:
        print(item + " ", end='')
    print("")
    
    
for i in range(11):
    print(str(i) + " x " + str(i) + " = " + str(i*i))
    
    
test_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in test_list:
    print(item)
    
    
for i in range(101):
    if i % 2==0:
        print(i)
        
# Im not also doing odd, its literally just (i % 2 != 0)
total = 0
for i in range(101):
    total += i

print("The sum of all numbers is " + str(total) + ".")

total_even = 0
total_odd = 0
for i in range(101):
    if i % 2 == 0:
        total_even += i
    else:
        total_odd += i
        
print("The sum of all evens is " + str(total_even) + "." + "And the sum of all odds is " + str(total_odd) + ".")

countries_containing_land = []
for item in countries:
    if "land" in item:
        countries_containing_land.append(item)
        
print(countries_containing_land)

# lmao why use a loop
fruit_list = ['banana', 'orange', 'mango', 'lemon']
fruit_list.reverse()
print(fruit_list)


languages = []

for item in data:
    for value in item.get("languages"):
        languages.append(value)
    
set_of_languages = set(languages)
print("total languages: " + str(len(set_of_languages)))

# going to assume 3.3.2 means the languages spoken in the most country, otherwise its impossible to find the answer with this dataset

lang_dict = {}

for lang in languages:
    lang_dict[lang] = 0

for item in data:
    for value in item.get("languages"):
        lang_dict[value] = lang_dict[value] + 1
        

most_spoken = []
for key,value in lang_dict.items():
    if len(most_spoken) < 11:
        most_spoken.append([key, value])
    else:
        for item in most_spoken:
            if item[0] != key:
                if item[1] < value:
                    del most_spoken[most_spoken.index(item)]
                    most_spoken.append([key, value])
                    break
                
most_spoken.sort(key=lambda x: x[1])
most_spoken.reverse()

for item in most_spoken:
    print(item[0] + ": Spoken in " + str(item[1]) + " countries.")

# Not doing 3.3.3 as it is an easier version of 2
