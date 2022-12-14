from data import *
from os import system
filename = 'arak.csv'
cimsor = ''


def menu():
    system('cls')
    print('0 - Kilép')
    print('1 - Sütik')
    print('2 - Új sütemény')
    print('3 - Törlés')
    return input('Választás: ')

def menu1():
    print('0 - Vissza a menübe')
    print('1 - Jelenleg kapható sütemények')
    print('2 - Legdrágább süti')
    print('3 - Legolcsóbb süti')
    print('4 - Sütemény keersése')
    return input('Választás: ')

def loadCookies():
    system('cls')
    file = open(filename, 'r', encoding='utf-8')
    global cimsor
    cimsor = file.readline() #címsor
    for row in file:
        splitted = row.strip().split(';')
        sutik[splitted[0]] = int(splitted[1])
    file.close()

def kaphatoSutik():
    system('cls')
    print('Kapható sütemények')
    for suti, ar in sutik.items():
        print(f'{suti} - {ar} Ft.')
    input('Tovább (Enter)...')

def ujSuti():
    system('cls')
    print('Új sütemény felvétele')
    suti = input('Süti: ')
    ar = (input('Ára: '))
    sutik[suti] = ar
    saveresultToFile(suti, ar)
    print('Sikeres felvétel.')
    input()

def saveresultToFile(suti, ar):
    system('cls')
    file = open(filename, 'a', encoding='utf-8')
    file.write(f'{suti};{ar}\n')
    file.close()

def deletcookies():
    system('cls')
    print('Eredmény törlése')
    suti = input('A törlendő süti: ')
    if suti in sutik:
        sutik.pop(suti)
        saveAllToFile()
        input('Süti törölve. Tovább (Enter)...')
    else:
        input('Nincs ilyen süti')

def saveAllToFile():
    system('cls')
    file = open(filename, 'w', encoding='utf-8')
    file.write(cimsor)
    for suti,ar in sutik.items():
        file.write(f'{suti};{ar}\n')
    file.close()

def legdragabb():
    system('cls')
    maxkey = ''
    maxvalue = 0
    for key,value in sutik.items():
        if value > maxvalue:
            maxvalue = value
            maxkey = key
    return maxkey

def legolcsobb():
    system('cls')
    minkey = ''
    minvalue = 9999999999999999
    for key,value in sutik.items():
        if value < minvalue:
            minvalue = value
            minkey = key
    return minkey

def search(needle):
    for nev,ar in sutik.items():
        if nev.upper() == needle.upper():
            return nev
    return False

