import random
def rand(start,stop):
    number1 = random.randint(start, stop)
    number2 = random.randint(start, stop)
    total = number1 + number2
    int(input(f"{number1} + {number2} = "))

    return number1, number2

def main():
    difficulty = int(input("What difficulty do you want? 1, 2, or 3?: "))
    if difficulty == 1:
        start = 1
        stop = 9
    if difficulty == 2:
        start = 10
        stop = 99
    if difficulty == 3:
        start = 100
        stop = 999
    
    rand(start,stop)

main()