from profanity import profanity


def read_txt_file():
    with open('bot.txt', 'r') as file:
        contents = file.read()
    return contents.strip()


def build_random_phrase_list():
    l = []
    contents = read_txt_file().split('\n')
    for i in contents:
        l.append(i)
    return l


def append_phrases(phrase):
    phrases = build_random_phrase_list()
    if phrase not in phrases:
        with open('bot.txt', 'a') as file:
            file.write(phrase + "\n")
