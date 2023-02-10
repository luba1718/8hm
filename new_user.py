import view
import o_list

o_list.OpenListW()

def Record(surname, name, first_name, post, salary, telephone, telegram):
    file = open('list.txt', 'a')   
    file.write(str(f"{surname};{name};{first_name};{post};{salary};{telephone};{telegram}\n"))
    file.close()
def NewEntry():
    print('ДОБАВЛЕНИЕ НОВОГО СОТРУДНИКА:---------------------------------------------------------')
    print('Отмена ввода: 0')
    print('--------------------------------------------------------------------------------------')
    introductory = ['Фамилия', 'Имя', 'Отчество', 'Должность', 'Оклад', 'Номер телефона (+7)', 'Telegram']
    intro = []
    for i in range(len(introductory)):
        text = str(input(f"{introductory[i]}: "))
        if text != '0':
            intro.append(text)
        else:
            view.Сlear()
            print('СОТРУДНИКИ:---------------------------------------------------------------------------')
            print('Все сотрудники: S | Добавить: + | Поиск: * | Основное меню: A')
            return 'S'
    
    Record(intro[0], intro[1], intro[2], intro[3], intro[4], intro[5], intro[6])
    view.Сlear()
    print('СОТРУДНИКИ:---------------------------------------------------------------------------')
    print('Все сотрудники: S | Добавить: + | Поиск: * | Основное меню: A')
