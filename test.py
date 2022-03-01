import csv
from datetime import date
from datetime import datetime


def age(birthdate):
    today = date.today()
    yearDifference = today.year - birthdate.year
    noBirthdayThisYear = (today.month, today.day) < (birthdate.month, birthdate.day)
    
    if noBirthdayThisYear :
        return yearDifference -1
    return yearDifference   

Name = input("pls enter ur name: ")
Lastname = input("pls enter ur Lastname: ")
birthday = input("pls enter ur birthday: ")

with open('data.csv', 'a') as file:
    myFile = csv.writer(file)
    myFile.writerow([Name, Lastname, birthday])
   
    birthdate = datetime.strptime(birthday, "%d.%m.%Y")
    
    if age(birthdate) > 17:
        writer.writerow([Name, Lastname, birthday])
    else:
        print("You are not over 18.")

print("Thx " +Name)


print(age(date(2000, 1, 1)))
        
        
    