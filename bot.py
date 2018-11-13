from core_bot import *


def greeting():
    print(
        '''_________    ________      ___           ___  __                       _______
|\___   ___\ |\   __  \    |\  \         |\  \|\  \                    |\  ___ \\
\|___ \  \_| \ \  \|\  \   \ \  \        \ \  \/  /|_    ____________  \ \   __/|
    \ \  \   \ \   __  \   \ \  \        \ \   ___  \  |\____________\ \ \  \_|/__
     \ \     \ \  \ \  \   \ \  \____    \ \  \\\\ \  \ \|____________|  \ \  \_|\ \\
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
        text = input(">>>: ")
        if text.lower() != "bye":
            if random_message() is "":
                print("No news is good news\n")
            else:
                print(random_message() + "\n")
        else:
            active = False
            print("\nSee ya later alligator")


def play_the_guessing_game():
    lives = 5
    active = True
    print("Guess the number!")
    while (active is True):
        text = input(">>>: ")
        if guessing_game(text) == True:
            print("Good Job!")
            active = False
        else:
            num = guessing_game(text)
            print("Sorry...Try again!")
            lives = lives - 1
            if lives == 0:
                active = False
                print('''The winning number was {}'''.format(num))


def main():
    greeting()
    # wyd()
    # crazy_talk()
    play_the_guessing_game()


if __name__ == "__main__":
    main()
