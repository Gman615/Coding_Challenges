def DecToHex(num1, num2, num3):
    str1 = ""
    # converts entered numbers into hex
    hex1 = hex(num1)
    hex2 = hex(num2)
    hex3 = hex(num3)
    # converts the hex into a string
    hexstr1 = str1.join(hex1)
    hexstr2 = str1.join(hex2)
    hexstr3 = str1.join(hex3)
    # each string has 0x in front of it, so hexstr[2:] deletes those two figures
    str2 = hexstr1[2:]
    # if the number entered is less than 10, add a 0 to the front of it as is the way hex is presented
    if num1 < 10:
        finalstr1 = "0" + str2
    else:
        finalstr1 = str2
    str3 = hexstr2[2:]
    if num2 < 10:
        finalstr2 = "0" + str3
    else:
        finalstr2 = str3
    str4 = hexstr3[2:]
    if num3 < 10:
        finalstr3 = "0" + str4
    else:
        finalstr3 = str4
    # concatenates the string vsriables
    print("#" + finalstr1 + finalstr2 + finalstr3)



int1 = int(input("Please enter a number 0-255: "))
int2 = int(input("Please enter a number 0-255: "))
int3 = int(input("Please enter a number 0-255: "))


DecToHex(int1, int2, int3)
