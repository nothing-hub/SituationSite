# This is a tool for @ir_cyber_mp and any copywriting is illegal
# ir_cyber_mp
# Nedpy
import os
from colorama import Fore
from pyfiglet import Figlet
import requests as r
os.system('cls')
os.system('clear') 

# neccesary
print(Fore.YELLOW + '''if you face with Error maybe your Error is betwean those error in next line!!''')
print(Fore.YELLOW + '''FILEMODE INVALIDHEADER PROXY FORBIDEN SSLERROR ..... ''')

# interview
f = Figlet(font='slant')
print(Fore.BLUE + f.renderText('Mp hack'))
print('                                 @ir_cyber_mp')
print('  ')

# Error handelling
try:
    lol = input(Fore.RED + 'Enter your site ------>>> ')
    lil = r.get(f'{lol}')
    lili = lil.status_code
    f = Figlet(font='banner3-D')
    print(f.renderText(f'{lili}'))
except r.exceptions.ConnectTimeout:
    f = Figlet(font='banner3-D')
    print(f.renderText('503'))
    print(Fore.RED + '''The request send but after a time dont answer!!!
    for more information GOOGLE the Error''')
except r.exceptions.ConnectionError:
    f = Figlet(font='banner3-D')
    print(f.renderText('url'))
    print(Fore.YELLOW + 'your url is invalid please make sure and write it again\nif you want!!')
    m = input('Do you want to run the tool again? y/n ---->>> ')
    if m == 'y' or m == 'yes':
        os.system('cls')
        os.system('python main.py')
    elif m == 'n' or m == 'no':
        f = Figlet(font='banner3-D')
        print(f.renderText('bye'))
        print('telegram: ir_cyber_mp')
    else:
        print('something went wrong!!')
except r.exceptions.MissingSchema:
    f = Figlet(font='banner3-D')
    print(f.renderText('HTTP HTTPS'))
    print('you forgrt them!!')
    m = input('Do you want to run the tool again? y/n ---->>> ')
    if m == 'y' or m == 'yes':
        os.system('cls')
        os.system('python main.py')
    elif m == 'n' or m == 'no':
        f = Figlet(font='banner3-D')
        print(f.renderText('bye'))
        print('telegram: ir_cyber_mp')
    else:
        print('something went wrong!!')

# use tool again
j = input('Do you want to run the tool again? y/n ---->>> ')
if j == 'y' or j == 'yes':
    os.system('cls')
    os.system('python main.py')
elif j == 'n' or j == 'no':
    f = Figlet(font='banner3-D')
    print(f.renderText('bye'))
    print('telegram: ir_cyber_mp')
else:
    print('something went wrong!!')
