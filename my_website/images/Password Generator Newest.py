#Password Generator

import random
print("*********************************")
print("*********************************")
print("Welcome to the Password Generator")
print("*********************************")
print("*********************************")


x = raw_input( "How many characters do you want in your password?")


def password(x):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+;':<>,.?/"
    mypw = ""

    for i in range(int(x)):
        next_index = random.randrange(len(characters))
        mypw = mypw + characters[next_index] 
    print ("Your new password is:", mypw)
        
if x >= 0:
    password(x)