import re
# this function takes in a string with no number and appends 1 automatically. If the number provided is greater than 1, it adds 1 to the number provided.
def StringAdder(string):
    # empty string variable, used for joining a list and converting
    str1 = ""
    # finds the number in the string provided by user
    result = re.findall(r'\d+',text)
    # joins list to make a string so that we can see how long the string is
    result1 = str1.join(result)
    # creates an integer of the length of the string number provided
    result2 = len(result1)
    # if the result of the integer search is empty list or nothing
    if result == [] :
        text1 = text + "1"
        print(text1)
    # otherwise, if its any integer of any length, this does what is needed
    else:
        text1 = text[:-result2]
        num = int(str1.join(result))
        num += 1        
        num1 = str(num)
        string = text1 + num1
        print(string)



text = input("Please ender a word with or without a positive number after\n") 
StringAdder(text)

