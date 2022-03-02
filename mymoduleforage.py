from datetime import date

def age(birthdate):
    
    today = date.today()
    yearDifference = today.year - birthdate.year
    noBirthdayThisYear = (today.month, today.day) < (birthdate.month, birthdate.day)
    
    if noBirthdayThisYear :
        return yearDifference -1
    return yearDifference   