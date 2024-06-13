def main():
    #print integers between 0 and 10:
    for number in range(11):
        print(number)

    #print integers between 5 and 10:
    print("\n\n")
    for number in range(5,11):
        print(number)

    #print even numbers between 0 and 10:
    print("\n\n")
    for number in range(0,11, 2):
        print(number)

    #prompt the user for start and stop values and print the numbers between them
    #get start value from the user as an integer
    print("\n")
    start = int(input("Enter what number you want to start at:"))

    #get stop value from the user as an integer
    stop = int(input("Enter what number you want to stop at:"))

    #use start and stop values in a for loop
    print("\n")
    for number in range(start,stop+1):
        print(number)

main()