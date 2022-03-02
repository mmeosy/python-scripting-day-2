import os

def osusing(name1, userdating):
    os.mkdir(name1)
    os.system("touch "+ name1 +"/.userdating.txt")
    os.system("echo " + name1 + userdating + ">>/userdating.txt")