#create a program to ask for payment for vending machine items
def main():
    due = 50
    while due > 0:
        try:
            print(f"Please pay {due} in coins:")
            payment = int(input("Please enter your coin payment in numbers of cents: "))
            if payment == 1 or payment == 5 or payment == 10 or payment == 25:
                due = due - payment
        except:
            continue
    if due < 0:
        print(f"You are owed {due * -1} cents")
main()