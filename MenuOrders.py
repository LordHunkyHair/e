def main():
    print(f"This is our menu:\nBaja Taco: 4.00\nBurrito: 7.50\nBowl: 8.50\nNachos: 11.00\nQuesadilla: 8.50\nSuper Burrito: 8.50\nSuper Quesadilla: 9.50\nTaco: 3.00\nTortilla Salad: 8.00")
    orders = {
        "BAJA TACO": 4.00,
        "BURRITO": 7.50,
        "BOWL": 8.50,
        "NACHOS": 11.00,
        "QUESADILLA": 8.50,
        "SUPER BURRITO": 8.50,
        "SUPER QUESADILLA": 9.50,
        "TACO": 3.00,
        "TORTILLA SALAD": 8.00
        }
    total = 0
    while True:
        try:
            print("\nItem:")
            order = str(input())
            if order.upper() in orders:
                total = total+orders[order.upper()]
                print(f"Total: ${total:.2f}")
            elif order.upper() == "END":
                break
            else:
                continue
        except:
            continue
main()