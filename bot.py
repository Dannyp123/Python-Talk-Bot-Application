from core_bot import *
import os
import requests
from profanity import profanity


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
    if name in ["Talk-E", "talk-e", "TALK-E", "Talk-e"]:
        print('''OMG... That is my name''' + '\n')
        print('''Anyways, {} nice to meet you\n'''.format(name))
    else:
        print(hello(name))


def home_screen():
    command_strings = ["1", "2", "3", "4", "5", "6", "--h"]
    help_info = "\t- (1) To find out how old I am!\n\t- (2) If you would like to hear a joke!\n\t- (3) If you wanna throw a party! (CTRL+C to stop the party!)\n\t- (4) If you would like to play a game!\n\t- (5) If you would like to hear a joke generated by the Interwebs!\n\t- (6) If you would like to leave!\n\tOr just talk to me!"
    greeting()
    print(help_info)
    print("--h to display this menu again")
    active = True
    while (active is True):
        text = input(">>>: ")
        if text not in command_strings:
            if profanity.contains_profanity(text):
                print("WATCH YO PROFANITY!!")
            else:
                append_phrases(text)
                print(random_message())

        elif text == "1":
            print(age())

        elif text == "2":
            print(get_jokes())

        elif text == "3":
            os.system('curl parrot.live')
            print('\n\n')

        elif text == "4":
            play_the_guessing_game()

        elif text == "5":
            url = 'https://icanhazdadjoke.com/'
            headers = {'Accept': 'application/json'}
            json = requests.get(url, headers=headers).json()
            print(json['joke'])

        elif text == '6':
            active = False
            print("\n" + "Goodbye" + "\n")

        elif text.lower() == "--h":
            print(help_info)


def play_the_guessing_game():
    lives = 5
    num = randint(1, 15)
    active = True
    print("Guess the number that is from 1 to 15 ONLY!")
    while (active is True):
        print()
        text = input(">>> ")
        if int(text) == num:
            print("Good Job You Guessed It!")
            active = False
        elif int(text) > 15:
            print("number must be between 1 and 15")
        else:
            print("Sorry...Try again!")
            lives = lives - 1
            if lives == 0:
                active = False
                print('''The winning number was {}'''.format(num))


def main():
    home_screen()


if __name__ == "__main__":
    main()
