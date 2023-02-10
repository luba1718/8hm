import view

def CommandProcessing():
    menu_number = ' '
    while menu_number != 'exit':
        view.Menu()
        menu_number = view.Team()
        if menu_number == 'S':
            view.Search()