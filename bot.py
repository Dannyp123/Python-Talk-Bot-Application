from core_bot import *


def greeting():
    name = input("What's your name? ")
    print(hello(name))


def wyd():
    what_are_they_doing = input("What are you doing? ")
    print(cool_bro(what_are_they_doing))

def main():
    greeting()
    wyd()


if __name__ == "__main__":
    main()
