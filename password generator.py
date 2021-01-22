import string
import random
#these are the keys that the computer can use to make the passswords 
characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
#this asks you how many and how long do you want your passwords to be
n = input ('how many passwords do you want?  ')
n = int (n)
l = input ('how long should it be? ')
l = int (l)
for p in range (n):
    password = ''
    for c in range (l):
      #this is the part of the code that randomises the password
        password += random.choice(characters)
        print (password)
print ('here is your custom password(s);)')