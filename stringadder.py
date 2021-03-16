import re
# this function takes in a string with no number and appends 1 automatically. If the number provided is greater than 1, it adds 1 to the number provided.
def StringAdder():
    text = input("Please ender a word with or without a positive number after\n")
    str1 = ""
    # finds the number in the string provided by user
    result = re.findall(r'\d+',text)
    # joins list to make an empty string
    result1 = str1.join(result)
    # creates an integer of the length of the string number provided
    result2 = len(result1)
    # if the result is empty list
    if result == [] :
        text1 = text + "1"
        print(text1)
        exit()
    text1 = text[:-result2]
    num = int(str1.join(result))
    num += 1        
    num1 = str(num)
    string = text1 + num1
    print(string)



    
StringAdder()
exit()
