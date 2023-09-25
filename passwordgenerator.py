import string
import random
 
 #function to print the password
def generator(length):
    passw=''
    for char in range(length):
        passw+= random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
    return passw
length=int(input("Enter the length of passw :"))
print(generator(length))

#function to print the passw with given characters
def chargen(words):
    ln=len(words)
    passw=""
    for char in words:
        passw+=random.choice(words)
    print(passw)
chargen("ABC")