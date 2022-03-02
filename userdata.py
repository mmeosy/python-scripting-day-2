
from datetime import datetime
def getuserdata():
    name = input("pls enter ur name: ")
    lastname = input("pls enter ur Lastname: ")
    birthday = input("pls enter ur birthday: ")
    birthdate = datetime.strptime(birthday, "%d.%m.%Y")
    return {"name":name, "lastname":lastname, "birthday":birthday, "birthdate":birthdate}