import random

print "Howdy, what's your name?"
name = raw_input()
print "Choose a random number between 1 and 100"
guessnumber = raw_input()
guessnumber = int(guessnumber)

mynumber = random.randint(1,100)

while guessnumber != mynumber:
    if guessnumber > mynumber:
        print "Your guess is too high, try again."
    else:
        print "Your guess is too low, try again."
    print "Your guess?"
    guessnumber = raw_input()
    guessnumber = int(guessnumber)
if guessnumber == mynumber:
    print "Congratulations!"