
from userdata import getuserdata
from mymoduleforage import age
import writingdata


userdata = getuserdata()

if age(userdata["birthdate"]) > 17:
    writingdata.writecsvfile([userdata["name"],userdata["lastname"], userdata["birthday"]])
else:
    print("You are not over 18.")

print("Thx " + userdata["name"])



        
        
    