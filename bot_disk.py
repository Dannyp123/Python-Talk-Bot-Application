def read_txt_file():
    with open('bot.txt', 'r') as file:
        contents = file.read()
    return contents

def build_random_phrase_list():
    list = []
    contents = read_txt_file().split('\n')
    for i in contents:
        list.append(i)
    return list

def append_phrases(phrase):
    list = build_random_phrase_list()
    if phrase not in list:
        with open('bot.txt', 'a') as file:
            file.write(phrase + "\n")
