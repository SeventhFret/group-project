
from os import system
from datetime import datetime, timedelta
#import pyjokes
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
        user_data = input('Please, input date in format[DD/MM/YYYY]: ')
        user_data.replace('/', ' ')
        
        user_date = datetime(int(user_data[6:]), int(user_data[3:4]), int(user_data[0:2]))
        print()
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        year=int(input("Enter Year: "))
        month=int(input("Enter Month Number: "))
        print(calendar.month(year,month))
    elif choice == "7":
        year = datetime.now().year
        if (year % 4 == 0):
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
        if (year % 4 ==0) and (year % 100 != 0):
            print("{0} is a leap year".format(year))
        
    elif choice == "8":
        inp_year = int(input("Give year:"))
        year = inp_year
        leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 == 0

        if leap:
            print(f"The next leap year from {year} is {year + 4}")

        while not leap:
            year += 1
            leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 == 0
            print(f"The next leap year from {inp_year} is {year}")
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