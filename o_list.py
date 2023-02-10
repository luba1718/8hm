import os.path

def OpenListW():
    check_file = os.path.isfile('list.txt')
    if check_file == False:
        file = open('list.txt', 'w')
        file.write(str(f"id;surname;name;first_name;post;salary;telephone;telegram\n"))
        file.close()