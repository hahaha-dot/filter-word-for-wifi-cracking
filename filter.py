import re
import os
import sys

os.system("clear")

def function():
   user = input("Please enter the path of the file ==>\n")
   if os.path.exists(user):
      with open(user, 'r') as r:
         read = r.read()
         repair = read.replace(" ", '')
         find = re.findall("\w{8}", repair)
         with open('/home/kali/Desktop/reslut2.txt', 'w') as w:
            w.write("The match is %s" % (find))
   else:
      sys.exit(1)
    
function()
