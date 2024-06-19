def main():
    while True:
        try:
            print("Equation:")
            equation = str(input())
            symbols = equation.split(" ")
            number1 = float(symbols[0])
            number2 = float(symbols[2])
            if symbols[1] == "+":
                total = number1 + number2
            if symbols[1] == "-":
                total = number1 - number2
            if symbols[1] == "*":
                total = number1 * number2
            if symbols[1] == "/" and number2 != 0:
                total = number1 / number2
            elif symbols[1] == "/" and number2 == 0:
                continue
            print(f"{total:.2f}")
            break
        except:
            continue
main()
while(True):
    repeat = input("\nDo you want to run the program again, y/n?:")
    if repeat == "y":
        main()
        continue
    elif repeat == "n":
       print("Program ending...")
       break
    else:
        print("Error: Please type the letter y for yes or n for no")