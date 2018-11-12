from bot_disk import *
from random import choice


def hello(name):
    return '''hello {}\nMy name is PyBot'''.format(name)


def cool_bro(wtd):
    return '''That is cool broski!\n{} is one of my favorite things to do!'''.format(
        wtd)


def randomMessage():
    random_phase = choice(build_random_phrase_list())
    return random_phase
