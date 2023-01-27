from os import system
import calendar
from datetime import datetime, timedelta
import pyjokes

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
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
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
        pass
    elif choice == "8":
        year = int(input())
        leap_year = calendar.isleap(year)

        if leap_year == True:
            year % 4 == 0 and (year % 100 or year % 400 == 0)
            print(year)
        else:
            print([y for y in range(year, year + 4) if calendar.isleap(y)])
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
