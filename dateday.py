#Determine Day of Week
def leapyearcheck(year):  # Function to check if it is a leapyear
    leapyear = False
    if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0) and (year % 400 == 0) and (year % 100 == 0)):
        leapyear = True
    else:
        leapyear = False
    return leapyear


def dayofdate(x):
    days = ["Saturday","Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] #List defining dates of the week
    thirty1day = [1, 3, 5, 7, 8, 10, 12]  # Serial no of months which have 31 days
    thirtyday = [4, 6, 9, 11]              # Serial no of months which have 30 days

    valid = False         #Boolean variable to check if the user input is valid. Initialised to false.
    if len(x) < 10:       #Since the "/" will also be taken into account. 
        print("Please try again and enter date in the format DD/MM/YYYY")
    else:
        date = int(x[0:2])      #Slices the date from string and stores it as an integer
        month = int(x[3:5])     #Slices the month from string and stores it as an integer
        year = int(x[6:])       #Slices year from string and stores it as an integer so that calculations can be made
             #Boolean variable to check if the year is a leapyear. Initialised to false


        if (month in thirty1day) and (date <= 31) and (date >= 1) and (month >= 1) and (month <= 12) and (year >= 1):
            valid = True
        elif (month in thirtyday) and (date <= 30) and (date >= 1) and (month >= 1) and (month <= 12) and (year >= 1):
            valid = True
        elif (month == 2) and (leapyearcheck(year) == True) and (date >= 1) and (date <= 29) and (year >= 1):
            valid = True
        elif (month == 2) and (leapyearcheck(year) == False) and (date >= 1) and (date <= 28) and (year >= 1):
            valid = True
        else:
            valid = False

        if not valid:
            dayofdate(input("Your previous entry was wrong. Please try again : "))
        else:
            leapcount = 0
            for i in range(1, year):
                if leapyearcheck(i) == True:
                    leapcount += 1
            daynum = ((year - 1) * 365) + leapcount
            if month == 1:
                daynum = daynum + date
            else:
                for i in range(1, month):
                    if i in thirty1day:
                        daynum = daynum + 31
                    elif i in thirtyday:
                        daynum = daynum + 30
                    elif (i == 2):
                        if leapyearcheck(year) == True:
                            daynum = daynum + 29
                        else:
                            daynum = daynum + 28
                daynum = daynum + date + 2
            dayofweek = days[(daynum % 7) - 1]
            print(x,"is a",dayofweek)


dayofdate(input("Enter date in the form of DD/MM/YYYY: "))


