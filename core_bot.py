from bot_disk import *
from random import choice

random_phase = build_random_phrase_list()


def hello(name):
    return '''hello {}\n My name is PyBot'''.format(name)


def cool_bro(wtd):
    return '''That is cool broski!\n {} is one of my favorite things to do!'''.format(
        wtd)


def randomMessage(inputs):
    if inputs != "bye":
        print(random_phase)
