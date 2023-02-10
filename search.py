import view
import o_list

def SearchList():
    o_list.OpenListW()
    view.Сlear()
    print('ПОИСК СОТРУДНИКА:---------------------------------------------------------------------')
    print('Все: S | Добавить: + | Поиск: * | Удалить: - | Редактировать: R | Экспорт: J | Меню: A')
    print('--------------------------------------------------------------------------------------')
    file1 = open('list.txt', 'r')
    file_text = list(file1)
    file1.close()
    print('ВЕСЬ СПИСОК (ENTER)')
    search = str(input('Поисковой запрос?: '))
    file2 = open('search.txt', 'w')
    for i, value in enumerate(file_text):
        if i != 0:
            if search in value:
                value = ''.join(value.replace(';', ' '))
                file2.write(f"{i} {value}")
    file2.close()
    print('--------------------------------------------------------------------------------------')
    file2 = open('search.txt', 'r')
    for j in file2:
        print(''.join(j.replace(';', ' ')))
    file2.close()