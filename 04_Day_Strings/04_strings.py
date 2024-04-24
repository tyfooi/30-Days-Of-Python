# Only doing the ones that aren't "elementary"

# 9
sentence = "Coding For All"
print(sentence[slice(0,6)])
# 10
if "Coding" in sentence:
    print("yes it is")
    
# 11
sentence_two = sentence.replace("Coding", "Python")
print(sentence_two)

# 13
split_sentence = sentence.split(" ")
print(split_sentence)

# 20
print(sentence.index("C"))

# 22 
print(sentence.rfind("l"))

# 25
sentence_long = 'You cannot end a sentence with because because because is a conjunction'
sliced_long = sentence_long.replace("because because because ","")
print(sliced_long)

# 26
print(sentence_long.index("because"))

# 28
if split_sentence[0] == "Coding":
    print('first substring is "Coding"')

# 30
fixed_sentence = '   Coding For All      '
fixed_sentence = fixed_sentence.strip(" ")
print(fixed_sentence)

# 32
split_sentence = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_sentence = " ".join(split_sentence)
print(joined_sentence)

# 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34
sequence = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(sequence.expandtabs(10))

# 35

print("radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.")

