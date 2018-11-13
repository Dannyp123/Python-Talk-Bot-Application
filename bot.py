from core_bot import *


def greeting():
    # print('_____    _____')
    # print('|    \\  /     |')
    # print('|___0|  |0____|')
    # print('     \\  /')
    # print('  ___|__|___')            'What do you call an elf that can sing? A wrapper.',

    # print('  |  ')
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
        text = input(">>>: ").strip()
        if "#age" in text.lower():
            print(age())
        elif text.lower() != "bye":
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


def help_menu():
    active = True
    print("--h for help menu")
    while (active is True):
        text = input(">>>: ")
        if text.lower() == "--h":
            print(
                "\t- #age for app's age\n\t- #joke for joke\n\t- any text besides '#age', '#joke','--h' will generate a random phrase\n\t- bye to leave"
            )
        elif text.lower() == "bye":
            active = False
            print("Goodbye")
        else:
            print("okay")


def main():
    greeting()
    # wyd()
    # crazy_talk()
    # play_the_guessing_game()
    help_menu()


if __name__ == "__main__":
    main()
