#functin to load menu items from the file and create a dictionary
def get_orders():
    #create a file handle that gives access to the file
    file = open("menu.txt", "r")

    #create an empty dictionary for possibble orders
    orders = {}

    #loop through data in the file and read the file 1 line at a time
    for line in file:

        #split the line of data
        order_and_prices = line.split(",")
        #get order and price from the list and put them in the dictionary
        order = order_and_prices[0]
        price = float(order_and_prices[1])
        orders[order] = price
    
    file.close()
    return orders

def main():
    orders = get_orders()
    print(f"This is our menu:\nBaja Taco: 4.00\nBurrito: 7.50\nBowl: 8.50\nNachos: 11.00\nQuesadilla: 8.50\nSuper Burrito: 8.50\nSuper Quesadilla: 9.50\nTaco: 3.00\nTortilla Salad: 8.00")
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