import cmath
import string

name = "Ayrat"
print("Hello {0}".format(name))
print("Hello " + name)

first_name = 'Joffrey'
greeting = 'Hello'
print(f'{greeting}, {first_name}!')
# => Hello, Joffrey!

text = '''Пример текста,
состоящего из
нескольких строк'''
print(text)


def sayName(name2, age):
    print(name2, age)


sayName(age=18, name2=name)

arr = [1, 2, 45, 7, 8]
summa = 0;

for i in arr:
    summa += i

obj = {
    "name": "Yura",
    "age": 17
}

print(obj["name"])
print(arr[0])


class User:
    name = "Ayrat"

    def getName(self):
        return self.name

    def setName(self, value):
        self.name = value


user = User()

print(user.getName())
user.setName(value="Yura")
print(user.getName())

stark = 'Arya'
print("Do you want to eat, {0}".format(stark) + "?\nYes, I'm hungry, mom.")

magic = '\nyou'
print(magic[1])  # => ?

print('Alexander'[-1])

one = 'Naharis'
two = 'Mormont'
three = 'Sand'

print(one[2] + two[1] + three[3] + two[4] + two[2])

print('Alexander'[3:7])  # xand
print('Alexander'[3:])  # xander
print('Alexander'[:7])  # Alexand
print('Alexander'[3:7:2])  # xn, здесь 2 - это шаг извлечения
print('Alexander'[::-1])  # rednaxelA

value = 'Hexlet'
print(value[2:5])

print(int('10'))
print(float(10))
print(str(10 > 5))

print(len('Alex'))  # => 4

print(pow(2, 3))  # => 8


def argss(*args):
    print(args)


argss(1, 2, 3)

print(type('haha'))

company = "hexlet"
print(company.capitalize())


def myFunc(x):
    return x


def passFunc():
    pass


def hf(a, b=6):
    return a + b


print(hf(4))


def truncate(string, remainedLength):
    return string[:remainedLength] + '...'


print(truncate('hahaha', 2))


def get_hidden_card(string, starsamount=4):  # "*1100"
    stars = "*" * starsamount
    cutted = string[-4:]
    print(cutted)
    return stars + cutted


print(get_hidden_card('12345678912', 5))


def named(a, b, c=7):
    print(a / b + c)


named(b=4, a=12)


def trim_and_repeat(text, offset=0, repetitions=1):
    return text[offset:] * repetitions


print(trim_and_repeat('python', offset=3, repetitions=2))


def get_age_difference(year1, year2):
    return f'The age difference is {abs(year2 - year1)}'


print(get_age_difference(2020, 1009))


def has_upper_case(word):
    return word.lower() != word


print(has_upper_case('Words'))
print(has_upper_case('woed'))
print(has_upper_case(''))


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


print(is_leap_year(2018))
print(is_leap_year(2017))
print(is_leap_year(2016))


def string_or_not(any):  # диспетчеризация
    keys = {
        'True': 'yes',
        'False': 'no',
    }
    return keys[str(isinstance(any, str))]


print(string_or_not('goof'))
print(string_or_not(9))

print('ALexander'.find('AL'))
print('ALexander'.find('Ax'))
print('ALexander'.find('and'))


def normalize_url(url):
    if url.startswith('https://'):
        return url
    elif url.startswith('http://'):
        return 'https://' + url[7:]
    else:
        return 'https://' + url


print(normalize_url('https://ya.ru'))  # 'https://ya.ru'
print(normalize_url('google.com'))  # 'https://google.com'
print(normalize_url('http://ai.fi'))  # 'https://ai.fi'


def print_numbers(num):
    while num:
        print(num)
        num -= 1
    print('finished!')


print_numbers(4)


def join_numbers_from_range(start, end):
    sum = ''
    while start <= end:
        sum += str(start)
        start += 1
    print(sum)


join_numbers_from_range(1, 6)
join_numbers_from_range(1, 1)


def my_substr(string, len):
    fin = ''
    for i in range(len):
        fin += string[i]
    return fin


print(my_substr('hello', 2))


def is_contains_char(word, char):
    if word.lower().find(char.lower()) == -1:
        return False
    return True


print(is_contains_char('hello', 'h'))
print(is_contains_char('hello', 'w'))
print(is_contains_char('hello', 'H'))


def sum(numbers):
    result = 0
    for num in numbers:
        result += int(num)
    return result


print(sum("12345"))  # 15


def filter_string(text, symbol):
    res_str = ''
    for index in range(0, len(text)):
        if text[index].lower() != symbol.lower():
            res_str += text[index]
    return res_str.strip()

text = 'If I look forward I win'
print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win

text2 = 'I look back if you are lost'
print(filter_string(text2, 'w')) # 'I look back if you are lost'
print(filter_string(text2, 'I')) # 'look back f you are lost'

def is_palindrome(text):
    if len(text) < 2:
        return True
    if text[0] == text[len(text)-1]:
        return is_palindrome(text[1:-1])
    return False

print ('is_palindrome')
print(is_palindrome(''))  # True пустая строка тоже считается палиндромом
print(is_palindrome('radar')) # True
print(is_palindrome('a')) # True
print(is_palindrome('abs')) # False
print(is_palindrome('ишак ищет у тещи каши')) # True

import main
main.doAction()

from main import doAction
doAction()

from symbols import is_vowel
def count_vowels(string):
    count = 0
    for letter in string:
        if is_vowel(letter):
            count += 1
    return count

print(count_vowels('a'))
print(count_vowels('abeu'))
print(count_vowels('abc'))

from for_import import *
showTwo()

import trainPack.constants
import trainPack.functions

trainPack.functions.func(trainPack.constants.WORD)
print(trainPack.NAME)

def choice_from_range(string, start=0, end=0):
    import random
    return string[random.randint(start, end)]

print(choice_from_range('abcds',2,4))

cortage = (1,2,3,4,5)

(one,two,three,four,five) = cortage

print(one)
print(two)
print(three)

def sort_pair(pair):
    if pair[0] > pair[1]:
        return (pair[1], pair[0])
    return (pair[0], pair[1])