from function import *

loadCookies()
choice = ''
while choice != '0':
    choice = menu()
    if choice =='1':
        kaphatoSutik()
    elif choice == '2':
        ujSuti()
