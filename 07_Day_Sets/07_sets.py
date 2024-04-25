it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Snapchat","Tiktok"])
print(it_companies)
it_companies.remove("Tiktok")
print("There is no null reference checking in discard.")

fruit = {"Apples", "Bananas", "Oranges"}

C = A.union(B)
print(A.intersection(B))
print(A.issubset(B))

a_with_b = A.union(B)
b_with_a = B.union(A)

print("Symmetric difference: " + str(A.symmetric_difference(B)))

del C,B,A,a_with_b,b_with_a,fruit

age_set = set(age)

if len(age) > len(age_set):
    print("list is bigger: " + str(len(age)))
    print("length of set: " + str(len(age_set)))
else:
    print("set is bigger: " + str(len(age_set)))
    print("length of list: " + str(len(age)))
    
sentence = "I am a teacher and I love to inspire and teach people."

sentence = sentence.split(" ")
sentence = set(sentence)
print(len(sentence))