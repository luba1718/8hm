import readline

def make_pre_input_hook(default):

    def pre_input_hook():
        readline.insert_text(default)
        readline.redisplay()
    return pre_input_hook

def Edit():
    print('РЕДАКТИРОВАНИЕ ДАННЫХ О СОТРУДНИКЕ:----------------------------------------------------')
    print('Все: S | Добавить: + | Поиск: * | Удалить: - | Редактировать: R | Экспорт: J | Меню: A')
    print('--------------------------------------------------------------------------------------')
    file = open('list.txt', 'r')
    file_text = list(file)
    file.close()
    edit = str(input('Введите id сотрудника: '))
    if edit != '' and edit != '0':
        edit = int(edit)
        for i, value in enumerate(file_text):
            value = ''.join(value.replace(';', ' '))
            if i == edit:
                file_text_edit = value.split()

    edit_list = ['Фамилия', 'Имя', 'Отчество', 'Должность', 'Оклад', 'Номер телефона (+7)', 'Telegram']

    for j  in range(len(edit_list)):
        readline.set_pre_input_hook(make_pre_input_hook(file_text_edit[j]))
        edit_list[j] = str(input(f'{edit_list[j]}: '))
    readline.set_pre_input_hook(make_pre_input_hook(''))

    file2 = open('list.txt', 'w')
    for k, value1 in enumerate(file_text):
        if k != edit:
            file2.write(value1)
        elif k == edit:
            edit_list = ';'.join(edit_list)
            file2.write(f'{edit_list}\n')
    file2.close()