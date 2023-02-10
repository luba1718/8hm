def OpenList():
    file = open('list.txt', 'r')
    file_text = list(file)
    for index, value in enumerate(file_text, 0):
        value = ''.join(value.replace(';', ' '))
        print(index, value)
    file.close()