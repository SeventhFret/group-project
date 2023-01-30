
from os import system
import calendar
from datetime import datetime, timedelta
#8import pyjokes

# CREATING MENU
choice = ''

while choice != 'x':
    system('clear')
    print('Welcome to brand-new software!'.center(50, '-'), end='\n\n')
    print('What do you want to do?\n')
    print('''[1] - Display current time
[2] - Display current time in UNIX format
[3] - Convert data to datetime format
[4] - Calculate the time from today to some future date
[5] - Show the delta
[6] - Display calendar for certain month
[7] - Is current year leap?
[8] - How much time to next leap year?
[9] - Random joke
[10] - Real-time clock
[x] - Exit program
''')

    choice = input()
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        year = 2023 
        #leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 == 0
        if (year % 4 == 0):
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
        if (year % 4 ==0) and (year % 100 != 0):
            print("{0} is a leap year".format(year))
    elif choice == "8":
        
        #inp_year = int(input("Give year:"))
        leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 == 0
        if leap:
            print(f"The next leap year from {year} is {year + 4}")
        while not leap:
            year += 1
            leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 == 0
            print(f"The next leap year is {year}")
    elif choice == "9":
        pass
    elif choice == "10":
        pass
    if choice != 'x':
        print('Press Enter to proceed...')
        input()
        continue
    else:
        print('Alright, see you!')

