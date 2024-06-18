def main():
    while True:
        try:
            print("Equation:")
            equation = str(input())
            numbers = equation.split(" ")
            if numbers[1] == " " and numbers[3] == " " and type.numbers[0] == int and type.numbers[4] == int and (numbers[2] == "+" or numbers[2] == "-" or numbers[2] == "*" or numbers[2] == "/"):
                number1 = int(numbers[0])
            else:
                break
        except:
            continue
main()