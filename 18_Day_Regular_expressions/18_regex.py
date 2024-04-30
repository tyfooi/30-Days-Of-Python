import re


paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
counts = [(len(re.findall(word, paragraph)),word) for word in paragraph.split()] # using regex is slower, so i didnt bother with re.split
#print(counts)


text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."
points = re.findall(r'[-+]?\d+',text)
print(points)
sorted_points = [int(char) for char in points]
print(sorted_points)
distance = (abs(int(points[0])-int(points[len(points)-1])))
print(distance)

# 2
# This is a bad use case, so im not doing it, slower, and complicated for no reason
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

sentence = re.sub(r"[%@&;$#]", '', sentence)
print(sentence)

counts = set([(len(re.findall(word, sentence)),word) for word in sentence.split()])
print(counts)
counts = sorted(counts, key=lambda x: x[0], reverse = True)
print(counts)
counts = counts[0],counts[1],counts[2]
print(counts)