#create a program that accepts a highway number and outputs a direction
def main():
    while True:
      try:
        highway = int(input("Please enter a highway number: "))
        if highway < 1:
            print("Error: Please enter a whole number:\n")
            continue
        if highway % 2 == 0:
            print(f"Highway {highway} goes from East to West")
        else:
            print(f"Highway {highway} goes from South to North")
      except:
         print("Error: Please enter a whole number:\n")
         continue
      break

main()

while(True):
    repeat = input("\nDo you want to run the program again, y/n?:")
    if repeat == "y":
        print()
        main()
        continue
    elif repeat == "n":
       print("Program ending...")
       break
    else:
        print("Error: Please type the letter y for yes or n for no")