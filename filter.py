import re
import os

os.system("clear")

def function() :
   with open('list.txt', 'r') as n:
      read = n.read()
      yes = read.replace(' ', '')
      print(yes.split())  
      find = re.findall("\w{8}", yes)
      with open('/home/kali/Desktop/result.txt', 'w') as t:
         t.write("The match is %s" % (find)) 

function()
