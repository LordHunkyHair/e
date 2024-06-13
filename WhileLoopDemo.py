def main():
    start = int(input("Enter what number you want to start at:"))
    stop = int(input("Enter what number you want to stop at:"))
    increment = int(input("Enter the increment you want between numbers:"))
    number = start
    #create while loop to print integers from 0-10
    while number <= stop:
        print(number)
        number += increment

main()