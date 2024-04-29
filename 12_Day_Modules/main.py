
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g, string_as_leet as st
from mymodule import random_user_id as randomuser, user_id_gen_by_user as userids, rbg_color_gen as rbg, generate_colors as pickcolor
from mymodule import random_number as rannumber
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

print("Leet speak: ")
print(st("happiness"))
print(randomuser())
print(userids(16,5))
print(rbg())

print(pickcolor("hexa",3))
print(pickcolor("rgb",4))

print(rannumber())
