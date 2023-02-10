import view
def Dell():
    view.Сlear()
    print('УДАЛЕНИЕ СОТРУДНИКА:------------------------------------------------------------------')
    print('Все сотрудники: S | Удалить сотрудника: - | Отмена: 0')
    print('--------------------------------------------------------------------------------------')
    file1 = open('list.txt', 'r')
    file_text = list(file1)
    file1.close()

    dell_line = str(input('Введите id сотрудника: '))
    if dell_line != '' and dell_line != '0':
        dell_line = int(dell_line)
        file2 = open('list.txt', 'w')
        for i, value in enumerate(file_text):
            value = ''.join(value.replace(';', ' '))
            if i != dell_line:
                file2.write(value)
        file2.close()
        if dell_line > i:
            print('Такого сотрудника нет!')
    else:
        print('Такого сотрудника нет!')