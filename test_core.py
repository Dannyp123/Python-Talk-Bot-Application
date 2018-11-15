from core_bot import *
from bcca.test import (
    should_print,
    fake_file,
)
from unittest import mock
from time import ctime

def test_phrase_dict():
    list = phrase_dict()
    list2 = phrase_dict()

    assert list == list2

@mock.patch('core_bot.randint')
def test_get_jokes_1(fake_num):
    fake_num.side_effect = [7]

    joke = get_jokes()

    assert joke == 'What do you call a pig that knows karate. Pork chop!'

@mock.patch('core_bot.randint')
def test_get_jokes_2(fake_num):
    fake_num.side_effect = [0]

    joke = get_jokes()

    assert joke == 'How many apples grow on a tree? All of them.'

def test_hello_1():
    name = 'Bob'

    greeting = hello(name)

    assert greeting == 'Hello Bob\nMy name is Talk-E!'

def test_hello_2():
    name = 'Sara'

    greeting = hello(name)

    assert greeting == 'Hello Sara\nMy name is Talk-E!'

def test_age():
    time = ctime()
    time = int(time.split()[-1]) - 2018
    phrase = "I'm {} years old!".format(time)

    bot_age = age()

    assert phrase == bot_age

@mock.patch('core_bot.randint')
def test_guessing_game_1(fake_num):
    fake_num.side_effect = [8]

    assert guessing_game('8') == True

@mock.patch('core_bot.randint')
def test_guessing_game_2(fake_num):
    fake_num.side_effect = [7]

    assert guessing_game('8') == False
