from datetime import datetime
from mymoduleforage import age
import writingdata




Name = input("pls enter ur name: ")
Lastname = input("pls enter ur Lastname: ")
birthday = input("pls enter ur birthday: ")

birthdate = datetime.strptime(birthday, "%d.%m.%Y")

if age(birthdate) > 17:
    writingdata.writecsvfile([Name, Lastname, birthday])
else:
    print("You are not over 18.")

print("Thx " +Name)


