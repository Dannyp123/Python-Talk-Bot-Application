from core_bot import *
import os
import requests
from profanity import profanity
from time import sleep
from termcolor import colored


def greeting():
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
        print('OMG... That is my name\nAnyways, Its nice to meet you {}\n.format(name)')
    else:
        print(hello(name))


def home_screen():
    command_strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "--h"]
    help_info = "\t- (1) To find out how old I am!\n\t- (2) If you would like to hear a joke!\n\t- (3) If you wanna throw a party! (CTRL+C to stop the party!)\n\t- (4) If you would like to play a game!\n\t- (5) If you would like to hear a joke generated by the Interwebs!\n\t- (6) To attempt to cross the Bridge!!\n\t- (7) To Talk to Forrest Gump!\n\t- (8) To release the Dancing Elves! \n\t- (9) If you would like to leave\n\tOr just talk to me!"
    greeting()
    print('{}\n--h to display this menu again'.format(help_info))
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
            print(requests.get('https://icanhazdadjoke.com', headers={'Accept': 'application/json'}).json()['joke'])

        elif text == "6":
            crossing_the_bridge()

        elif text == "7":
            talking_with_Gump()

        elif text == "8":
            release_the_elves()

        elif text == '9':
            active = False
            print("\n" + "Goodbye" + "\n")

        elif text.lower() == "--h":
            print(help_info)


def play_the_guessing_game():
    lives = 4
    num = randint(1, 100)
    active = True
    print("Guess the number that is from 1 to 100 ONLY!")
    while (lives != 0):
        print()
        text = input(">>> ")
        if text.isdigit():
            lives = lives - 1
            if lives == 0:
                active = False
                print("Sorry... :-(")
                print('''The winning number was {}'''.format(num))
                print("\n" + "To play again, hit 4 or hit --h to see menu")
            elif int(text) == num:
                print("Good Job You Guessed It!")
                print("To play again, hit 4 or hit --h to see menu" + "\n")
                lives = 0
                active = False
            elif int(text) > 100:
                print("number must be between 1 and 100")
            elif int(text) < num:
                print("\n" + "Guess Up")
            elif int(text) > num:
                print("\n" + "Guess Down")
        else:
            print("Must be a number sir or madam")


def talking_with_Gump():
    name = input("Hey there, what is your name? ")
    print("Hey {}, my name is Forrest Forrest Gump".format(name) + "\n")
    print(
        "Mama always said that life is like a box of chocolate... you never know what you gonna get!!"
        + "\n")
    chocolate = input(
        "Did you know that life is like a box of chocolate... you never know what you gonna get!!"
        + "\n")
    if chocolate in ["yeah", "yes", "yah", "Yes"]:
        print("Awesome, we can be like two peas in a pod" + "\n")
        sleep(2)
        print("It was nice meeting you {}".format(name))

    else:
        print("Darn, Oh well now you know, lets go see Jen-ney")
        print("I just love Ping Pong\n")
    vietnam = input("Who is the best Ping Pong master? ")
    if vietnam in ["you", "You", "Forrest", "Forrest Gump"]:
        print("You got that right {}".format(name))
    else:
        print("You just dont know...oh well!")


def crossing_the_bridge():
    print("HALT!")
    name = input("What is your name?\n>>>: ")
    quest = input("What is your quest?\n>>>: ")
    swallows = input("What is the air-speed velocity of an unladen swallow?")
    if did_they_cross(name, quest, swallows) != True:
        print("*You have been flung into the Gorge of Eternal Peril*")
    else:
        print("You have successfully crossed the bridge!")


def release_the_elves():
    text = colored(
        '''

8888888b.         d8888 888b    888  .d8888b. 8888888 888b    888  .d8888b.        8888888888 888    888     888 8888888888  .d8888b.
888  "Y88b       d88888 8888b   888 d88P  Y88b  888   8888b   888 d88P  Y88b       888        888    888     888 888        d88P  Y88b
888    888      d88P888 88888b  888 888    888  888   88888b  888 888    888       888        888    888     888 888        Y88b.
888    888     d88P 888 888Y88b 888 888         888   888Y88b 888 888              8888888    888    Y88b   d88P 8888888     "Y888b.
888    888    d88P  888 888 Y88b888 888         888   888 Y88b888 888  88888       888        888     Y88b d88P  888            "Y88b.
888    888   d88P   888 888  Y88888 888    888  888   888  Y88888 888    888       888        888      Y88o88P   888              "888
888  .d88P  d8888888888 888   Y8888 Y88b  d88P  888   888   Y8888 Y88b  d88P       888        888       Y888P    888        Y88b  d88P
8888888P"  d88P     888 888    Y888  "Y8888P" 8888888 888    Y888  "Y8888P88       8888888888 88888888   Y8P     8888888888  "Y8888P"

    ''',
        'green',
        attrs=['reverse', 'blink'])
    print(text)


def main():
    home_screen()


if __name__ == "__main__":
    main()
