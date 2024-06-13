def main ():
    #create lists
    names = ["John", "Mary", "Alice", "Bob"]
    integer_list = [10, 16, 24, 42, 14, 9]
    random_list = ["Cyd", 15, 22.3, "Frank"]

    print(names)
    print(integer_list)

    #add values to a list
    names.append("Jonny")
    integer_list.append(5)
    integer_list.append(63)

    print(names)
    print(integer_list)

    #get the number of items in a list
    items_amount = len(integer_list)
    print(f"\nNumber of items in integer list: {items_amount}")

    #get values from our list
    #get the first value from the integer list
    print(f"\nFirst item in integer list: {integer_list[0]}")

    #get the fourth value from the integer list
    print(f"\nFourth item in integer list: {integer_list[3]}")

    #print all items in the integer list
    print("\nInteger list items:")
    for item in integer_list:
        print(item)

    print()
    for index in range(items_amount):
        print(f"Index {index+1}: {integer_list[index]}")

main()