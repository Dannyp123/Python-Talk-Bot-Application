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

@mock.patch('core_bot.ctime')
def test_age_1(time):
    time.side_effect =['2019'] 

    bot_age = age()

    assert bot_age == "I'm 1 years old!"

@mock.patch('core_bot.ctime')
def test_age_2(time):
    time.side_effect =['2025'] 

    bot_age = age()

    assert bot_age == "I'm 7 years old!"

@mock.patch('core_bot.randint')
def test_guessing_game_1(fake_num):
    fake_num.side_effect = [8]

    assert guessing_game('8') == True

@mock.patch('core_bot.randint')
def test_guessing_game_2(fake_num):
    fake_num.side_effect = [7]

    assert guessing_game('8') == False

@fake_file({'bot.txt': '''line1
line2
line3
'''})
@mock.patch('core_bot.choice')
def test_random_message_1(choice):
    choice.side_effect = ['line2']

    assert random_message() == 'line2'

@fake_file({'bot.txt': '''line1
line2
line3
'''})
@mock.patch('core_bot.choice')
def test_random_message_2(choice):
    choice.side_effect = ['line3']

    assert random_message() == 'line3'

def test_did_they_cross_1():
    name = 'Bob'
    quest = ''
    swallows = ''

    did_they_cross(name, quest, swallows) == False

def test_did_they_cross_2():
    name = 'Arthur'
    quest = ''
    swallows = ''

    did_they_cross(name, quest, swallows) == True

def test_did_they_cross_3():
    name = 'Arthur'
    quest = 'Nothing'
    swallows = ''

    did_they_cross(name, quest, swallows) == False

def test_did_they_cross_4():
    name = 'Arthur'
    quest = 'To seek the Holy Grail'
    swallows = ''

    did_they_cross(name, quest, swallows) == True

def test_did_they_cross_5():
    name = 'Arthur'
    quest = 'To seek the Holy Grail'
    swallows = 'None'

    did_they_cross(name, quest, swallows) == False

def test_did_they_cross_6():
    name = 'Arthur'
    quest = 'To seek the Holy Grail'
    swallows = 'An African or European swallow?'

    did_they_cross(name, quest, swallows) == True
