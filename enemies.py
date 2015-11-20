# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

# функция проверки целого числа на простоту
def isprime(n):
        # 0 и 1 не являются простыми
        if n < 2:
            return False
        # 2 единственное из четных является простым
        if n == 2:
            return True
        # все остальные четные составные
        if not n & 1:
            return False
        # начиная с 3 и до корня из n
        # по всем нечетным числам
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                return False
        return True
# функция разложения простого числа на простые множители
def decompose(n):
    Arr=[]
    while n>1 and n%2==0:
        Arr.append(2)
        n=n//2
    if n>1:
        for i in range(3, int(n**0.5)+1, 2):
            if isprime(i):
                while n>1 and n%i==0:
                    Arr.append(i)
                    n=n//i
    if n>1: # если n оказалось простым
        Arr.append(n)
    return Arr

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    name = 'дракон'
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return int(answer) == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest
class RedDragon (Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
    

<<<<<<< HEAD
# красный дракон учит вычитанию, а чёрный -- умножению.
class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

#FIXME класс Троллей
class Troll(Enemy):
    name = 'тролль'


class FirstTroll(Troll):
    '''
    троль предлагает угадать число от 1 до 5
    '''
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'загадочный'

    def question(self):
        x = randint(1,5)
        self.__quest = 'Угадай целое число от 1 до 5'
        self.set_answer(x)
        return self.__quest

    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return int(answer) == self.__answer


class SecondTroll(Troll):
    '''
    троль предлагает угадать проверить число на простоту
    '''
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'простой'

    def question(self):
        x = randint(1,100)
        self.__quest = 'Число '+str(x)+' простое или составное?'
        # проверим, какое число x
        if isprime(x):
            self.set_answer('простое')
        else:
            self.set_answer('составное')
        return self.__quest

    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer): # изменим проверку ответа -
        return  answer.strip().lower()==self.__answer

class ThirdTroll(Troll):
    '''
    троль предлагает разложить число на простые множители
    '''
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'фактурный'

    def question(self):
        x = randint(1,100)
        self.__quest = 'Разложи число '+str(x)+' на простые множители (ответ через запятую)'
        # сам троль должен разложить число x на множители
        # answer станет списком простых
        self.set_answer(decompose(x))
        return self.__quest

    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer): # переопределение метода из базового класса - у нас здесь своя реализация
        # соберем из строки ответа список простых множителей и проверим
        Arr=list(map(int,answer.split(',')))
        x=1 # посчитаем произведение чисел из ответа героя
        for i in Arr:
            x*=i
        y=1 # посчитаем произведение чисел задуманных тролем
        for i in self.__answer:
            y*=i

        if x==y and len(Arr)==len(self.__answer):
            for i in Arr: # поищем соответствие
                if i not in self.__answer:
                    return False
            return True
        else:
            return False




enemy_types = [GreenDragon, RedDragon, BlackDragon, FirstTroll, SecondTroll, ThirdTroll]
