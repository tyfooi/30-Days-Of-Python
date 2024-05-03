import json
import re
from collections import Counter


def file_details(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f = open(filename, "r")
    txt = f.read().replace(",","").replace("..."," ").replace(".","").replace("-","").replace(";","").replace("\n","").split(' ')
    txt = list(filter(None, txt))
    f.close()
    return ("lines: " + str(len(lines)) + "\nUnique words: " + str(len(txt)))


def most_spoken_languages(json_file,range):
    f = open(json_file,'r',encoding='utf-8')
    data = json.load(f)
    # data = json.dumps(data)   
    lang_set = [lang for item in data for lang in item['languages']]
    f.close()
    # BASICALLY: first n items of a 'SORTED' 'LIST' of 'COUNTS' of 'ITEMS' from a 'DICT' in 'REVERSE ORDER'
    return sorted(list(Counter(lang_set).items()), key=lambda x: x[1], reverse = True)[:range]
    

print(most_spoken_languages('./data/countries_data.json',10))

def most_populated_countries(json_file, range):
    f = open(json_file,'r',encoding='utf-8')
    data = json.load(f)
    countries_pop = [{'country':country['name'],'population':country['population']}for country in data]
    #print(countries_pop)
    f.close()
    return [item for item in sorted(countries_pop, key=lambda d: d['population'],reverse = True)][:range]

print(most_populated_countries('./data/countries_data.json',10))


f = open('./data/email_exchanges.txt')
# BASICALLY: readlines{list} return only if start with 'From', split that sentence, return email, remove '\n'
emails = set([(item.split(" "))[1].replace("\n","") for item in f.readlines() if item.startswith('From')])
print(emails)

# 2 is something we've basically done before

def find_most_frequent_words(txt_file,range):
    f = open(txt_file, 'r',encoding = 'utf-8')
    #txt = ' '.join(f.read().replace(","," ").replace("..."," ").replace('"',"").replace("."," ").replace("-"," ").replace(";"," ").replace("  "," ").replace("  "," ").replace("\n","").replace(":"," ").replace("["," ").replace("]"," ").replace("!"," ").replace("?"," ").split(' ')).split()
    return Counter((' '.join(e for e in f.read().split() if e.isalnum())).split()).most_common(range)
    # print(txt)
    #return Counter(txt).most_common(10)
    
# find_most_frequent_words('./data/obama_speech.txt',10)
print(find_most_frequent_words('./data/obama_speech.txt',10))


def check_similarity(txt_file1, txt_file2):
    f = open(txt_file1, 'r',encoding = 'utf-8')
    stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're",
                  "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he',
                  'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's",
                  'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
                  'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is',
                  'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',
                  'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as',
                  'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
                  'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
                  'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
                  'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
                  'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own',
                  'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't",
                  'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',
                  "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't",
                  'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't",
                  'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't",
                  'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    txt1 = list(Counter(' '.join(e.lower() for e in f.read().split() if e.isalnum()).split()))
    # txt1 = [txt1.remove(e) for e in txt1 if e in stop_words]
    for element in txt1:
        for item in stop_words:
            if element in item:
                txt1.remove(element)
                break
    f = open(txt_file2, 'r',encoding = 'utf-8')
    txt2 = list(Counter(' '.join(e.lower() for e in f.read().split() if e.isalnum()).split()))
    for element in txt1:
        for item in stop_words:
            if element in item:
                txt1.remove(element)
                break
    f.close()

    
    count = 0
    if len(txt1) > len(txt2):
        for word in txt2:
            if word in txt1:
                count+= 1
                txt1.remove(word)
                txt2.remove(word)
        return (round((count/len(txt1)),2)*100)
    elif len(txt1) < len(txt2):
        for word in txt1:
            if word in txt2:
                count+= 1
                txt2.remove(word)
                txt1.remove(word)
        return (round((count/len(txt2)),2)*100)
    else:
        for word in txt1:
            if word in txt2:
                count+= 1
                txt2.remove(word)
                txt1.remove(word)

        return (round((count/len(txt2)),2)*100)
    

print("percent similar:",check_similarity('./data/melina_trump_speech.txt','./data/michelle_obama_speech.txt'))
#check_similarity('./data/melina_trump_speech.txt','./data/michelle_obama_speech.txt')

# last two are easy so im not doing