import re
document=input("Message here:")
pattern=r"([a-z0-9\-.]+)@([a-z0-9\-.]+)\.(\w{1,3}$)|([a-z0-9\-.]+)@([a-z0-9\-.]+)\.(\w{2,3}$])\.(\w{2,3}$)"
match=re.search (pattern,document)
if match:
   print("valid")
   print(match.group())
else:
   print("Invalid email")
  
   #********Password Validation*****#
password=input("Entre a password:")
formt=r"([a-zA-Z0-9-.%&$@*]{12,16}$)"
check=re.search(formt,password)
if check:
  print("Strong")
  print(check.group())
else:
  print("Weak password")
 
#************Substitution*******#
string=input("Enter a sentence:")
ptn=r"boy"
newS=re.sub(ptn,"Keeeeny!",string,count=0)
print(newS) 
