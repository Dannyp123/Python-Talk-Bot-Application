from core_bot import *
from bcca.test import (
    should_print,
    fake_file,
)

def test_phrase_dict():
    list = phrase_dict()
    list2 = phrase_dict()

    assert list == list2
