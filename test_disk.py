from bot_disk import *
from bcca.test import (
    should_print,
    fake_file,
)

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
