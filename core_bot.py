from bot_disk import *
from random import choice, randint
from time import ctime


def phrase_dict():
    phrases = {
        'jokes': [
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
    return phrases


def get_jokes():
    phrases = phrase_dict()
    jokes = phrases["jokes"]
    i = randint(0, (len(jokes) - 1))
    return jokes[i]


def hello(name):
    return '''Hello {}\nMy name is Talk-E!'''.format(name)


def random_message():
    random_phrase = choice(build_random_phrase_list())
    return random_phrase


def guessing_game(text):
    num = randint(1, 15)
    if int(text) == num:
        return True
    else:
        return False


def age():
    time = ctime()
    return "I'm {} years old!".format(int(time.split()[-1]) - 2018)


def did_they_cross(name, quest, swallows):
    if name != "Arthur" or quest != "To seek the Holy Grail" or swallows != "An African or European swallow?":
        return False
    else:
        return True
