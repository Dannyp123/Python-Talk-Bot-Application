from bot_disk import *
from random import choice, randint
from time import ctime


def hello(name):
    return '''Hello {}\nMy name is Talk-E!'''.format(name)


def cool_bro(wtd):
    return '''That is cool broski!\n{} is one of my favorite things to do!'''.format(
        wtd)


def random_message():
    random_phase = choice(build_random_phrase_list())
    return random_phase


def guessing_game(text):
    num = randint(1, 15)
    if text == num:
        return True
    else:
        return False


def age(text):
    if "age" in text:
        time = ctime()
        return "I'm {} years old!".format(int(time.split()[-1]) - 2018)
