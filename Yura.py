import cmath

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

print(truncate('hahaha',2))