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
    if name in ["Talk-E", "talk-e", "TALK-E", "Talk-e"]:
        print('\n' + "OMG... we must be family")
        print('''Anyways, {}'''.format(hello(name)) + '\n')
    else:
        print(hello(name))


# def wyd():
#     active = True
#     while (active is True):
#         what_are_they_doing = input("What are you doing? ")
#         if what_are_they_doing.lower() != "bye":
#             print(cool_bro(what_are_they_doing))
#         else:
#             active = False
#             print("Goodbye")

# def crazy_talk():
#     active = True
#     while (active is True):
#         text = input(">>>: ").strip()
#         if "1" in text.lower():
#             print(age())
#         elif text == "5":
#             if random_message() is "":
#                 print("No news is good news\n")
#             else:
#                 print(random_message() + "\n")
#         else:
#             active = False
#             print("\nSee ya later alligator")


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
                "\t- (1) for app's age\n\t- (2) for joke\n\t- (3) to leave\n\t- (4) for Bot Mini Game\n\t- (5) for an highly enjoyed time"
            )
        elif text == "1":
            print(age())

        elif text == "2":
            # print('{}'.format(os.system('curl -H "Accept: text/plain" https://icanhazdadjoke.com/')))
            # response = requests.get('https://icanhazdadjoke.com/')
            # print(response.headers)
            # url = 'https://icanhazdadjoke.com/'
            # headers = {'Content-Type': 'text/plain'}
            # print(requests.get(url, headers=headers).content)

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
    greeting()
    # wyd()
    # crazy_talk()
    help_menu()


if __name__ == "__main__":
    main()
