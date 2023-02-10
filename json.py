def JSON(team):
    print('ЭКСПОРТ ДАННЫХ ИЗ ПОИСКОВОГО ЗАПРОСВ В JSON:------------------------------------------')
    print('Все: S | Добавить: + | Поиск: * | Удалить: - | Редактировать: R | Экспорт: J | Меню: A')
    print('--------------------------------------------------------------------------------------')
    print('Данные успешно экспортированы в файл search.json')
    file_search = open('search.txt', 'r')
    file_text = list(file_search)
    file_search.close()

    file_json = open('search.json', 'w')
    file_json.write('{ "staff": [\n')
    simvol1 = '{'
    simvol2 = '}'
    for i, value in enumerate(file_text, 1):
        value = value.split()
        if len(file_text) > i:
            file_json.write(f'{simvol1} "id": {i}, "surname": "{value[1]}", "name":"{value[2]}", "first_name": "{value[3]}", "post":"{value[4]}", "salary": "{value[5]}", "telephone": "+7 {value[6]}",  "telegram": "{value[7]}" {simvol2},\n')
        else:
            file_json.write(f'{simvol1} "id": {i}, "surname": "{value[1]}", "name":"{value[2]}", "first_name": "{value[3]}", "post":"{value[4]}", "salary": "{value[5]}", "telephone": "+7 {value[6]}",  "telegram": "{value[7]}" {simvol2}\n')
    file_json.write(']}')
