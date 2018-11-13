from bot_disk import *
from random import choice, randint
from time import ctime


def phrase_dict():
    phrases = {
        'bye': ["See ya later aligator"],
        'hi': ["Hello"],
        'joke': [
            'How many apples grow on a tree? All of them.',
            'What do you call an elf that can sing? A wrapper.',
            "Want to hear a joke about construction? I'm still working on it.",
            "The shovel was a ground-breaking invention.",
            "My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.",
            "Can February March? No, but April May.",
            "Did you know the first French fries weren't actually cooked in France? They were cooked in Greece.",
            "What do you call a pig that knows karate. Pork chop!", "MY LIFE"
        ]
    }


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
    if int(text) == num:
        return True
    else:
        return False


def age(text):
    if "age" in text:
        time = ctime()
        return "I'm {} years old!".format(int(time.split()[-1]) - 2018)
