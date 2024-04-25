empty_tuple = ()
fruit_tuple = ("apples", "bananas", "oranges")
meat_tuple = ("chicken", "beef", "pork")
food_tuple = fruit_tuple + meat_tuple
print(food_tuple)
print(len(food_tuple))

food_tuple = food_tuple + ("broccoli", "asparagus")
print(food_tuple)

food_list = list(food_tuple)
print(food_list)
food_list = food_list[3:len(food_list)-3]
print(food_list)

del food_tuple

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if "Estonia" in nordic_countries:
    print("Estonia is a nordic country.")
    
if "Iceland" in nordic_countries:
    print("Iceland is a nordic country.")