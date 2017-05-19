"""
    Program that outputs date of birth,
    including the exact day of the week,
    given the user's age and birthday
"""
import calendar
import datetime

month_dates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Get the user's age
while True:
    age = input("How old are you? (Reply with digits)\n")
    if age.isnumeric() and int(age) % 1 == 0 and int(age) > 0:
        break

    print("Try again")

print("\nWhen is your birthday?")
# Get the user's month of birth
while True:
    month = input("\nMonth(1 - 12):   ")
    if month.isnumeric() and int(month) % 1 == 0 and 0 < int(month) < 13:
        break

    print("Try again")


month_of_birth = int(month)


# Get the user's date of birth
while True:
    date = input("\nDate(1 - 31):   ")
    if date.isnumeric() and int(date) % 1 == 0 and 0 < int(date) < 32:

        if int(date) <= month_dates[int(month) - 1]:
            year_of_birth = int(datetime.date.today().year) - int(age)
            
            
            if int(month) == 2 and int(date) == 29 and calendar.isleap(year_of_birth):
                break
            
            elif int(month) == 2 and int(date) == 29 and not(calendar.isleap(year_of_birth)):
                print("This date does not exist.")

            else:
                break
                
        else:
            print("This date does not exist!")

    print("Try again")

date_of_birth = int(date)


if (int(month) - int(datetime.date.today().month)) > 0:
    year_of_birth -= 1

if (int(month) - int(datetime.date.today().month)) == 0:
    if (int(date) - int(datetime.date.today().day)) > 0:
        year_of_birth -= 1

day_of_birth = calendar.weekday(year_of_birth, month_of_birth, date_of_birth)
    

print("\nYou were born on " + str(calendar.day_name[day_of_birth]) + " "
      + str(date_of_birth) + " " + str(calendar.month_name[month_of_birth]) + " " + str(year_of_birth) + "  ! ! !")
