from countries_data import data

def add_two_numbers(n1, n2):
    return n1 + n2

    
# Honestly Im just gonna do the higher level stuff



def evens_and_odds(n):
    odds = 0
    evens = 0
    for i in range(n):
        if n % 2 == 0:
            evens+=1
        else:
            odds+=1
    output = "The number of odds are " +str(odds) + "\n" + "The number of evens are " + str(evens)
    return output

def factorial(n):
    for i in range(n,n+1):
        fact = fact * i



def most_spoken_languages():
    languages = []

    for item in data:
        for value in item.get("languages"):
            languages.append(value)
        
        
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


def most_populated_countries():
    countries = []
    for item in data:
        countries.append([(item.get("name")), (item.get("population"))])
    
    countries.sort(key=lambda x: x[1])
    countries.reverse()
    
    for i in range(21):
        print(str(i) + ".) " + countries[i][0] + " population: " + str(countries[i][1]) + " people.")

    
    
most_populated_countries()