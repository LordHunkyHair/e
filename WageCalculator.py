#write a program to calculate the annual wage of the user
#write two functions to get positive numbers from the user
def get_positive_hours():
  #ask user to enter their time worked per day
  #if bad input, reprompt user
  user_hours = 0
  while(True):
    try:
      user_hours = float(input("Enter your hours worked per day:"))
      #check if user_hours > 0 or greater than 24. If not, reprompt user
      if user_hours <= 0:
        print("Error: Please enter a number greater than 0 and less than 24")
        continue
      elif user_hours > 24:
         print("Error: Please enter a number greater than 0 and less than 24")
         continue
      else:
        break
    except:
      print("Error: Please enter a number greater then 0 and less than 24")
      
  return user_hours
def get_positive_pph():
  #ask user to enter their pay per hour
  #if bad input, reprompt user
  user_pph = 0
  while(True):
    try:
      user_pph = float(input("Enter your pay per hour:"))
      #check if user_hours > 0. If not, reprompt user
      if user_pph <= 0:
        print("Error: Please enter a number greater than 0")
        continue
      else:
        break
    except:
      print("Error: Please enter a number greater then 0")
      
  return user_pph

#INPUT
#get hours worked and pay per hour from function
user_hours = get_positive_hours()
user_pph = get_positive_pph()

#PROCESSING
#use a calculation to multiply them together and by 350 days
days_worked = 350
pretax_wage = user_hours * user_pph * days_worked

#calculate the amount taxed from the pretax_wage, and the new total
yearly_tax = 0.88
taxed_wage = pretax_wage * yearly_tax
taxed_income = pretax_wage - taxed_wage

#OUTPUT
#print output to the user
##Pay Advice:
print(f"Pay Advice\n---------------\nHours worked per day: {user_hours:.2f} hours\nPay per hour: ${user_pph:.2f}\nWages before taxes: ${pretax_wage:.2f}\nTaxed Income: ${taxed_income:.2f}\nTotal wage: ${taxed_wage:.2f}")