def main():
    #capitalize a string
    first_name = "Jacob"
    last_name = "Lohmeyer"
    print(first_name.capitalize())

    #make a string uppercase
    print(first_name.upper())

    #make a string lowercase
    print(f"{first_name.capitalize()} {last_name.lower()}")

    #determine if a string starts with a set of characters
    print(first_name.startswith("J"))

    if not first_name.startswith("J") and not first_name.startswith("j"):
        print(f"You spelled {first_name} wrong")
    else:
        print(f"You spelled {first_name} right")
    
    #determine if a string ends with a specified set of characters
    print(first_name.endswith("b"))

    #find a set of characters in a string
    print(first_name.find("c")+1)

    #loop through a string
    print()
    for letter in first_name:
        print(letter)
    
    print(f"{first_name} has {len(first_name)} letters")

    for letter_index in range(len(first_name)):
        print(f"Letter {letter_index+1}: {first_name[letter_index]}")

    print()
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #write code that counts how many times the word dog is said in sentence
    #use a while loop to read the string
    #start at the beggining
    #read until finding the word dog
    #add 1 to the number of found dogs
    #continue reading from the next index
    dogs = 0
    for index_number in range(len(sentence)):
        sentence.find("dog", index_number)
        if sentence.find("dog", index_number) == index_number:
            dogs += 1
    print(f"The word dog is used {dogs} times in this sentence.")

    #how to use the split method
    car_info = "Ferrari,F-50,2021,500000,4.8"
    car_data = car_info.split(",")
    print(car_data)

    #get the individual items from the resulting list
    car_make = car_data[0]
    car_model = car_data[1]
    car_year = int(car_data[2])
    car_value = float(car_data[3])
    car_engine = float(car_data[4])

    print(f"\nCar Information:\nMake: {car_make}\nModel: {car_model}\nYear: {car_year}\nValue: {car_value}\nEngine Size: {car_engine}")

main()