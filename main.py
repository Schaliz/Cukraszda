from function import *

loadCookies()
choice = ''
while choice != '0':
    choice = menu()
    if choice =='1':
        choice1 = ''
        while choice1 != '0':
            choice1 = menu1()
            if choice1 == '1':
                kaphatoSutik()
                input()
            elif choice1 == '2':
                print('A legdrágább süti neve: ',legdragabb())
                input('Tovább (Enter)')
            elif choice1 == '3':
                print('A legolcsóbb süti neve: ',legolcsobb())
                input('Tovább (Enter)')
    elif choice == '2':
        ujSuti()
    elif choice == '3':
        deletcookies()