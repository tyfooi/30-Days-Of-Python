import statistics
import math

basic_list = [1,2,3,4,5,6,7]
print(len(basic_list))

print(str(basic_list[0]) + str(basic_list[3]) + str(basic_list[6]))

companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle and Amazon."]

companies.append("Nvidia")
companies[1] = companies[1].upper()

it_string = "#".join(companies)
print(it_string)

if "Facebook" in companies:
    print("this is true")
    
companies.sort()
print(companies)
companies.reverse()
print(companies)

print(companies[2:len(companies)])

companies.remove(companies[round(len(companies)/2)])
print(companies)

for company in companies:
    companies.remove(company)

print(companies)
del companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end

print(joined_list)

full_stack = joined_list

full_stack_add = "Python", "SQL"

full_stack[(full_stack.index("Redux")+1):(full_stack.index("Redux")+1)] = full_stack_add
print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
max_min_age = max(ages),min(ages)
ages[len(ages):len(ages)] = max_min_age
print(ages)
print("Median: " + str(statistics.median(ages)))
print("Sum: " + str(sum(ages)))
print("Range : " + str((max(ages)-min(ages))))
print("abs of min-mean: " + str(abs(min(ages)-statistics.mean(ages))))
print("abs of max-mean: " + str(abs(max(ages)-statistics.mean(ages))))

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']

def get_middle(alist):
    if len(alist) % 2:
        return_value = alist[math.floor(len(alist)/2)], alist[math.ceil(len(alist)/2)]
        return return_value
    else:
        return alist[math.ceil(len(alist)/2)]
    
print(get_middle(countries))

if len(countries) % 2:
    split_list = [countries[0:math.floor(len(countries)/2)],countries[math.ceil(len(countries)/2):0]]
else:
    split_list = [countries[0:math.ceil(len(countries)/2)],countries[math.ceil(len(countries)/2)+1:0]]

a,b,c,*scandic = countries

print(str(a) + str(b) + str(c))
print("Scandic: " + str(scandic))