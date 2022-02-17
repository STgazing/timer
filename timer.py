from imaplib import Int2AP
import os
import platform
import time
from tracemalloc import start

#this is color class
class color:
    Green = '\033[92m'
    Cyan = '\033[96m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    

#this func show banner
def banner():
    print('''
▀█▀ █ █▀▄▀█ █▀▀ █▀█
░█░ █ █░▀░█ ██▄ █▀▄
''')
    print(f'{color.Cyan+"Follow us in github:"} {color.Cyan+"https://github.com/STgazing"}')
    print('''
''') 

#this func show menu bar
def menu():
    print(color.Green+'[',color.Yellow+'1',color.Green+']' , color.Cyan+'Limited Timer')
    print(color.Green+'[',color.Yellow+'2',color.Green+']' , color.Cyan+'Unlimited Timer')
    print(color.Green+'[',color.Yellow+'3',color.Green+']' , color.Cyan+'Exit')
    print('')

choose = None

#this class is time codes
class tmer:
    #this func is limited timer in menu bar
    def lim_timer():
        tmr = 0
        ss = int(input(f'{color.Green+"["} {color.Yellow+"+"} {color.Green+"]"} {color.Cyan+"Please set the timer in secconds: "}{color.Yellow+""}'))
        starting()
        while tmr < ss:
            print('')
            print('Press Ctrl + c to exit program')
            tmr+=1
            time.sleep(1)
            clear()
            print(f'{color.Magenta+"-->"} {color.Yellow+str(tmr)} {color.Magenta+"sec"}')
        print('')    
        print(color.Green+'Finished')
        print('')

    #this func is unlimited timer in menu bar
    def unlim_timer():
        tmr = 0
        starting()
        while True:
            print('')
            print('Press Ctrl + c to exit program')
            tmr+=1
            time.sleep(1)
            clear()
            print(f'{color.Magenta+"-->"} {color.Yellow+str(tmr)} {color.Magenta+"sec"}')

#this func takes you to the selected item in menu bar        
def cond():
    if choose == 1:
        tmer.lim_timer()
    elif choose == 2:
        tmer.unlim_timer()
    elif choose ==3:
        print('')
        print('See You Later :)')
        print('')
        quit()
    else:
        run()

#this func clear screen
def clear():
    ops = platform.system()
    if ops == 'Windows':
        os.system('cls')
    elif ops == 'Linux' or ops == 'Darwin':
        os.system('clear')
    else:
        os.system('cls' and 'clear')
#this func show a message before starting timer
def starting():
    a = reversed(list(range(4)))
    for i in a:
        clear()
        print(f'{color.Cyan+"Timer will be started in"} {color.Yellow+str(i)} {color.Cyan+"sec"}')
        time.sleep(1)
    clear()    
    print('Go!')    
        
#this func run program again
def tryagain():
    msg = input(color.Cyan+'Do yo want try again? Y/n: ')
    if msg.upper() == 'Y':
        run()
    elif msg.upper() == 'N':
        print()
        print(color.Yellow+'See You Later :)')
        print('')
        quit()
    else:
        tryagain()   
#this func is running the main program
def run():
    clear()
    global choose
    banner()
    menu()
    choose = int(input(f'{color.Green+"["} {color.Yellow+"+"} {color.Green+"]"} {color.Magenta+"Please choose an item:"}{color.Yellow+""} '))
    cond()
    tryagain()
    
run()
