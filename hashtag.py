
# this function takes a user input and capitalizes every word in the input
# removes spaces between words if there are any,
# and adds a hashtag to the beginning,
# also counts if string length is between 0-140
def createHashtag(string):
    strlength = len(string)
    if strlength >= 140:
        print("Your sentence is too long")
    elif strlength == 0:
        print("Please enter something.")        
    else: 
        result = ' '.join(elem.capitalize() for elem in string.split())
        hashtag = result.replace(" ", "")
        print("#" + hashtag)


    


















userinput = input("Please enter a word, phrase, or sentence\n")


createHashtag(userinput)

input("Press enter to exit ")
