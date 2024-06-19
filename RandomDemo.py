import random
def main():
    #print random number between 1-10
    random1 = random.randint(1,10)
    print(f"Random number: {random1}\n")

    #generate 10 random numbers between 1-10
    for count in range(10):
        random2 = random.randint(1,9)
        print(f"Random number {count+1}: {random2}")

    #choose a random value from a list
    random_list = [4,7,10,23,44,28,9,12]
    random_index = random.randint(0,len(random_list)-1)
    print(f"\nRandom index: {random_index}")
    print(f"Random list value: {random_list[random_index]}")

    #ask a user for the start and stop values for a random number generator
    #also ask how many numbers, and then generate it
    request = int(input("\nHow many numbers should be generated: "))
    start = int(input("What is the starting value: "))
    stop = int(input("What is the stopping value: "))
    for count2 in range(request):
        random3 = random.randint(start,stop)
        print(f"Random value {count2+1}: {random3}")

main()