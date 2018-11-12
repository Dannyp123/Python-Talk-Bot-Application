from core_bot import *


def greeting():
    # print('_____    _____')
    # print('|    \\  /     |')
    # print('|___0|  |0____|')
    # print('     \\  /')
    # print('  ___|__|___')
    # print('  |  ')
    print(
        '''_________    ________      ___           ___  __                       _______
|\___   ___\ |\   __  \    |\  \         |\  \|\  \                    |\  ___ \\
\|___ \  \_| \ \  \|\  \   \ \  \        \ \  \/  /|_    ____________  \ \   __/|
    \ \  \   \ \   __  \   \ \  \        \ \   ___  \  |\____________\ \ \  \_|/__
     \ \  \   \ \  \ \  \   \ \  \____    \ \  \\\\ \  \ \|____________|  \ \  \_|\ \\
      \ \__\   \ \__\ \__\   \ \_______\   \ \__\\\\ \__\                  \ \_______\\
       \|__|    \|__|\|__|    \|_______|    \|__| \|__|                   \|_______|
''')
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


def crazy_talk():
    active = True
    while (active is True):
        text = input(">>> ")
        if text.lower() != "bye":
            print(random_message() + "\n")
        else:
            active = False
            print("\nSee ya later alligator")


def main():
    greeting()
    # wyd()
    crazy_talk()


if __name__ == "__main__":
    main()
