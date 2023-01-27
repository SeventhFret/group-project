from os import system
from datetime import datetime, timedelta
import pyjokes
import calendar


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
        date = datetime.utcnow()
        utc_time = calendar.timegm(date.utctimetuple())
        print("Current time in UNIX format is: ", utc_time)
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        year=int(input("Enter Year: "))
        month=int(input("Enter Month Number: "))
        print(calendar.month(year,month))
    elif choice == "7":
        year = 2023     
        if year % 4 == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    elif choice == "8":
        pass
    elif choice == "9":
        print(pyjokes.get_joke())
    elif choice == "10":
        pass
    if choice != 'x':
        print('Press Enter to proceed...')
        input()
        continue
    else:
        print('Alright, see you!')
