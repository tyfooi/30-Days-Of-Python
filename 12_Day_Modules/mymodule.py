from random_word import RandomWords
import string
import random



def generate_full_name(firstname, lastname):
      space = ' '
      fullname = firstname + space + lastname
      return fullname

def sum_two_nums (num1, num2):
    return num1 + num2


gravity = 9.81
person = {
    "firstname": "Asabeneh",
    "age": 250,
    "country": "Finland",
    "city":'Helsinki'
}


def string_as_leet(s): # this is much more fun than 1.1
    leet_dict = {"s":"5","l":"1","e":"3","a":"4","t":"7","o":"0","z":"2","i":"!"}
    for char in s:
        if char in leet_dict.keys():
            s = s.replace(char,leet_dict.get(char))
    return s

def random_user_id():
    return string_as_leet((RandomWords().get_random_word()).capitalize()+"_"+(RandomWords().get_random_word()).capitalize())


def user_id_gen_by_user(chars, outputs):
    output_string = ""
    for i in range(outputs):
        word = ""
        for n in range(chars):
            letter = random.choice(string.ascii_letters)
            word += letter
        output_string += word + "\n"
    return output_string

def rbg_color_gen():
    return [random.randint(0,255),random.randint(0,255),random.randint(0,255)]



def generate_colors(format, numbers):
    characters = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    output_list = []
    if format.lower() == "hexa":
        for i in range(numbers):
            output_list.append("#"+characters[random.randint(0,len(characters)-1)]+characters[random.randint(0,len(characters)-1)]+characters[random.randint(0,len(characters)-1)]+characters[random.randint(0,len(characters)-1)]+characters[random.randint(0,len(characters)-1)]+characters[random.randint(0,len(characters)-1)])
    elif format.lower() == "rgb":
        for i in range(numbers):
            output_list.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    return output_list


def random_number():
    number_list = [0,1,2,3,4,5,6,7,8,9]
    output = ""
    for i in range(7):
        ran = random.randint(0,len(number_list)-1)
        output += str(number_list[ran])
        number_list.remove(number_list[ran])
    return output