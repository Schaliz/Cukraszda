from function import *

loadCookies()
choice = ''
while choice != '0':
    choice = menu()
    if choice =='1':
        kaphatoSutik()
    elif choice == '2':
        ujSuti()
    elif choice == '3':
        print('A legdrágább süti neve: ',legdragabb())
        input('Tovább (Enter)')
    elif choice == '4':
        print('A legolcsóbb süti neve: ',legolcsobb())
        input('Tovább (Enter)')
    elif choice == '5':
        deletcookies()