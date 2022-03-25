import random


# takes user input on length of password
def randomPW(length):
    randchar = 'a A b B c C d D e E f F g G h H i I j J k K l L m M n N o O p P q Q r R s S t T u U v V w W x X y Y z Z 1 2 3 4 5 6 7 8 9 0 ~ ` ! @ # $ % ^ & * _ - + = < > ?'.split()
    #alpha = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    #upperalpha = alpha.upper()
    # below line of code grabs a random sample from the string above which is 12 digits long
    #randupper = random.sample(upperalpha, length)
    randchar1 = random.sample(randchar, length)
    # removes the spaces and brackets form the generated code
    randchar1 = ''.join(randchar1)
    print(randchar1)




passwordLength = int(input("How long would you like your password to be?\n"))
randomPW(passwordLength)
