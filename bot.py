from core_bot import *
import os
import requests


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
     \ \  \   \ \  \ \  \   \ \  \____    \ \  \\\\ \  \ \|____________|  \ \  \_|\ \\
      \ \__\   \ \__\ \__\   \ \_______\   \ \__\\\\ \__\                  \ \_______\\
       \|__|    \|__|\|__|    \|_______|    \|__| \|__|                   \|_______|
''')
    name = input("What's your name? ")
    print(hello(name))


def home_screen():
    greeting()
    active = True
    while (active is True):
        text = input(
            "\t- (1) To find out how old I am!\n\t- (2) If you would like to hear a joke!\n\t- (3) If you wanna throw a party! (CTRL+C to stop the party!)\n\t- (4) If you would like to play a game!\n\t- (5) If you would like to leave!\n\tOr just talk to me!\n>>>: "
        )

        if text == "1":
            print(age())

        elif text == "2":
            print(get_jokes())

        elif text == "3":
            os.system('curl parrot.live')

        elif text == "4":
            play_the_guessing_game()

        elif text == '5':
            active = False
            print("\n" + "Goodbye" + "\n")
        else:
            print(random_message())


def play_the_guessing_game():
    lives = 5
    num = randint(1, 15)
    active = True
    print("Guess the number!")
    while (active is True):
        print()
        text = input(">>> ")
        if int(text) <= 15 and int(text) == num:
            print("Good Job!")
            active = False
        elif int(text) > 15:
            print("number must be between 1 and 15")
        else:
            print("Sorry...Try again!")
            lives = lives - 1
            if lives == 0:
                active = False
                print('''The winning number was {}'''.format(num))


def help_menu():
    active = True
    print("? for help menu")
    while (active is True):
        text = input(">>>: ")
        if text.lower() == "?":
            print(
                "\t- (1) for app's age\n\t- (2) for joke\n\t- (3) to leave\n\t- (4) for Bot Mini Game\n\t- (5) for a discussion with me"
            )
        elif text == "1":
            print(age())

        elif text == "2":
            url = 'https://icanhazdadjoke.com/'
            headers = {'Accept': 'application/json'}
            json = requests.get(url, headers=headers).json()
            print(json['joke'])
            
        elif text == "3":
            active = False
            print("\n" + "Goodbye" + "\n")

        elif text == "4":
            play_the_guessing_game()

        elif text == '5':
            os.system('curl parrot.live')
        else:
            print(random_message())


def main():
    home_screen()


if __name__ == "__main__":
    main()
