
from datetime import datetime
from mymoduleforage import age
import writingdata
import os



name = input("pls enter ur name: ")
lastname = input("pls enter ur Lastname: ")
birthday = input("pls enter ur birthday: ")
def osusing(name1):
    os.mkdir(name)
    os.system("touch "+ name+"/.userdating.txt")
    os.system("echo " + name + ">>/userdating.txt")

birthdate = datetime.strptime(birthday, "%d.%m.%Y")

if age(birthdate) > 17:
    writingdata.writecsvfile([name, lastname, birthday])
else:
    print("You are not over 18.")

print("Thx " +name)



        
        
    