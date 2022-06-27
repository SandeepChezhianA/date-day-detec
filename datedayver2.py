print ("Please enter the date in numerical format.")

date = int(input("Enter the date (dd): "))
month = int(input("Enter the month (mm): "))
year = int(input("Enter the year (yyyy): "))

if (year < 1) or (month < 1) or (date < 1):
    print ("Invalid input!")
    
if (month > 12):
    print ("Invalid input month!")

elif (date > 31):
    print("Invalid input date!")

elif (month == 2) and (year % 4 != 0):
    if date > 28:
        print ("Invalid input date!")
        
elif (month == 2) and (year % 4 == 0):
    if date > 29:
        print ("Invalid input date!")
        
elif (month == 4) or (month == 6) or (month == 9) or (month ==11):
    if date > 30:
        print ("Invalid input date!")
        
final = 0
final = final + date

if (month == 2):
    final = final + 31
    
elif (month == 3):
    final = final + 59
    
elif (month == 4):
    final = final + 90
    
elif (month == 5):
    final = final + 120
    
elif (month == 6):
    final = final + 151
    
elif (month == 7):
    final = final + 181
    
elif (month == 8):
    final = final + 212
    
elif (month == 9):
    final = final + 243
    
elif (month == 10):
    final = final + 273
    
elif (month == 11):
    final = final + 304
    
elif (month == 12):
    final = final + 334


        
