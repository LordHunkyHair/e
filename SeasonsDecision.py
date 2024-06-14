#function to return the season based on the month
#input: month number
#output: season name
def season2(month_again):
    if month_again == 12 or month_again <= 2:
        season = "Winter"
    elif month_again <= 5:
        season = "Spring"
    elif month_again <= 8:
        season = "Summer"
    elif month_again <= 11:
        season = "Fall"
    return season

def main():
#create a decision structure to determine the season based on the month
    months = ["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
    while True:
      try:
        month = int(input("Please enter the month number between 1 and 12: "))
        season = season2(month)
        if month < 1 or month > 12:
            print("Error: Please enter a whole number between 1 and 12:\n")
            continue
        if month == 12 or month <= 2:
            print(f"The month is {months[month-1]} and the season is {season}")
        elif month <= 5:
            print(f"The month is {months[month-1]} and the season is {season}")
        elif month <= 8:
            print(f"The month is {months[month-1]} and the season is {season}")
        elif month <= 11:
            print(f"The month is {months[month-1]} and the season is {season}")
      except:
          print("Error: Please enter a whole number between 1 and 12:\n")
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