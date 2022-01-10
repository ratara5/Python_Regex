#RANGES
import re

names_list=['Ana',
            'Pedro',
            'María',
            'Rosa',
            'Sandra',
            'Celia']

for elem in names_list:
    if re.findall('[o-t]',elem): #print all elements contains one or various literals from 'o' at 't', including. Case detection by default
        print(elem)
print('---------------------------------')

for elem in names_list:
    if re.findall('^[O-T]',elem): #print all elements that start with any literal from 'O' at 'T', including. Case detection by default
        print(elem)
print('---------------------------------')

for elem in names_list:
    if re.findall('[o-t]$',elem): #print all elements that end with any literal from 'o' at 't', including. Case detection by default
        print(elem)
print('---------------------------------')


###########APPLICATION WITH ENTERPRISE CODES##############
codes_list=['Ma1',
            'Se1',
            'Ma2',
            'Ba1',
            'Ma3',
            'Va1',
            'Va2',
            'Ma4',
            'MaA',
            'MaB',
            'MaC']

for code in codes_list:
    if re.findall('Ma[1-3]',code): #print all elements that contain any number from '1' at '3', including, and that start with 'Ma'. Case detection by default
        print(code)
print('---------------------------------')

for code in codes_list:
    if re.findall('Ma[^1-3]',code): #print all elements that NO contain any number from '1' at '3', including, and that start with 'Ma'. Case detection by default
        print(code)
print('---------------------------------')

for code in codes_list:
    if re.findall('Ma[1-3A-B]',code): #print all elements that contain any number from '1' at '3' or contain any literal from 'A' at 'B', including, and that start with 'Ma'. Case detection by default
        print(code)
print('---------------------------------')

###########APPLICATION WITH ENTERPRISE CODES##############
codes_list=['Ma.1',
            'Se1',
            'Ma2',
            'Ba1',
            'Ma:3',
            'Va1',
            'Va2',
            'Ma4',
            'Ma.A',
            'MaB',
            'MaC']

for code in codes_list:
    if re.findall('Ma[1-3.:A-B]',code):  #print all elements that contain any number from '1' at '3' or contain any '.' or ':' or contain any literal from 'A' at 'B', including, and that start with 'Ma'. Case detection by default
        print(code)
print('---------------------------------')