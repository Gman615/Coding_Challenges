import random


# takes user input on length of password
def randomPW(length):
    randchar = 'a A b B c C d D e E f F g G h H i I j J k K l L m M n N o O p P q Q r R s S t T u U v V w W x X y Y z Z 1 2 3 4 5 6 7 8 9 0 ~ ` ! @ # $ % ^ & * _ - + = < > ?'.split()
    # below line of code grabs a random sample from the string above which is 12 digits long
    randchar = random.sample(randchar, length)
    # removes the spaces and brackets form the generated code
    randchar = ''.join(randchar)
    print(randchar)




passwordLength = int(input("How long would you like your password to be?\n"))
randomPW(passwordLength)
