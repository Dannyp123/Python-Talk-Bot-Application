def read_txt_file():
    with open('bot.txt', 'r') as file:
        contents = file.read()
    return contents

def build_random_phrase_dict():
    list = []
    contents = read_txt_file()
    for i in contents:
        list.append(i)
    return list

