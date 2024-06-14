#function to add 2 numbers
#input: (int)number1, (int)number2
#output: (int)total
def add_numbers(number1, number2):
    total = number1 + number2
    c = 7
    return total

def main():
    a = 5
    b = 4
    c = 3
    #call add numbers function and assign the returned value to answer
    answer = add_numbers(a,b)
    print(f"{a} + {b} = {answer}\nVariable c = {c}")

main()