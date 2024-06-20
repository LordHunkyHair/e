import random
def rand(start,stop):
    number1 = random.randint(start, stop)
    number2 = random.randint(start, stop)
    correct = 0
    incorrect1 = 0
    incorrect2 = 0
    while True:
        try:
            total = number1 + number2
            answer = int(input(f"{number1} + {number2} = "))
            if answer == total:
                print("Correct!")
                correct += 1
                break
            elif answer != total:
                incorrect1 += 1
                if incorrect1 == 3:
                    print(f"Incorrect! The answer was {total}")
                    incorrect2 +=1
                    break
                print("Incorrect!")
                continue
        except:
            continue
    return correct

def main():
    correctomundo = 0
    while True:
        try:
            difficulty = int(input("What difficulty do you want? 1, 2, or 3?: "))
            if difficulty == 1:
                start = 1
                stop = 9
            elif difficulty == 2:
                start = 10
                stop = 99
            elif difficulty == 3:
                start = 100
                stop = 999
            else:
                continue
            while True:
                try:
                    questions = int(input("How many questions do you want between 3 through 10: "))
                    if questions != 3 and questions != 4 and questions != 5 and questions != 6 and questions != 7 and questions != 8 and questions != 9 and questions != 10:
                        continue
                    for amount in range (questions):
                        correct = rand(start,stop)
                        correctomundo += correct
                    print(f"You got {(correctomundo/questions)*100:.2f}% correct")
                    break
                except:
                    continue
        except:
            continue
        break
main()