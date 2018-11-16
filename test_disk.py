from bot_disk import *
from bcca.test import (
    should_print,
    fake_file,
)
from unittest import mock


@fake_file({'bot.txt': '''line
line
line
line
'''})
def test_read_txt_file_1():
    assert read_txt_file() == 'line\nline\nline\nline'


@fake_file({'bot.txt': ''})
def test_read_txt_file_2():
    assert read_txt_file() == ''


@fake_file({'bot.txt': '''line
line
line
line
'''})
def test_build_random_phrase_list_1():
    assert build_random_phrase_list() == ['line', 'line', 'line', 'line']


@fake_file({'bot.txt': ''})
def test_build_random_phrase_list_2():
    assert build_random_phrase_list() == ['']

@fake_file({'bot.txt': '''line1
line2
line3
'''})
def test_append_phrases_1():
    phrase = 'line4'
    phrase2 = 'line2'
    append_phrases(phrase)
    append_phrases(phrase2)

    assert open('bot.txt').read() == 'line1\nline2\nline3\nline4\n'

@fake_file({'bot.txt': '''line1
line2
line3
'''})
def test_append_phrases_2():
    phrase = 'line3'
    phrase2 = 'line2'
    append_phrases(phrase)
    append_phrases(phrase2)

    assert open('bot.txt').read() == 'line1\nline2\nline3\n'
