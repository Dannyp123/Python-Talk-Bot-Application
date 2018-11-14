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
def test_read_txt_file() :
    assert read_txt_file() == 'line\nline\nline\nline\n'
