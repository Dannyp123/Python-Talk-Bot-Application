from core_bot import *


def greeting():
    name = input("What's your name? ")
    print(hello(name))


def wyd():
    active = True
    while (active is True):
        what_are_they_doing = input("What are you doing? ")
        if what_are_they_doing.lower() != "bye":
            print(cool_bro(what_are_they_doing))
        else:
            active = False
            print("Goodbye")


def main():
    greeting()
    wyd()


if __name__ == "__main__":
    main()
