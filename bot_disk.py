def read_txt_file():
    with open('bot.txt', 'r') as file:
        contents = file.read()
    return contents
