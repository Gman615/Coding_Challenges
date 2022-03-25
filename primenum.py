def primeNum(num):
    prime = " is a prime number"
    notprime = " is not a prime number"
    if num == 1 or num == 2 or num == 3 or num == 5 or num == 7:
        print(str(num) + prime)
    elif num % 2 != 0 and num % 3 !=0 and num % 5 != 0 and num % 7 != 0:
        print(str(num) + prime)
    else:
        print(str(num) + notprime)










if __name__ == "__main__":
    userinput = int(input("Please enter a number\n"))
    primeNum(userinput)
    input("Please push enter to close program")
