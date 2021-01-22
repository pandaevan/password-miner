#this asks you to put in the password to see how long it would take hakers to get to yours
p = input ('type in a password to see how long it would take hackers to steal your password ')
import time
startTime = time.time()
#the code above is for a timer
#these are the tools we need to import into this module
import itertools
import string
#this is the part that tells the code if the password is correct
def password(true):
#this tells the computer what letters or numbers can be used
    characters = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    attempts = 0
    for length in range(1,9):
        #this tells the computer to repeate untill the password if found
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == true:
            #this tells you what the password is, how many guesses it took, and the amount of time
                return 'the password is {}. it was found in {} guesses.'.format(guess, attempts)
#this is where you put the password that the computer will try to guess no spaces but other than that its fine    
print(password(p))
executionTime = (time.time() - startTime)
print('time to find in seconds: ' + str(executionTime))