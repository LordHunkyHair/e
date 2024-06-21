import Automobile as Auto
#function to load vehicle data from a file
#Input: path to the file
#Output: list of automobiles
def load_vehicles(file_name):
    auto_list = []

    #open the file
    file = open(file_name, "r")

    #ignore the header in the file
    file.readline()

    #read each line of the file in a for loop
    line_number = 1
    for line in file:
        #increment line_number by 1
        line_number += 1

        #split the lines at the commas
        vehicle_data = line.split(",")

        #check that vehicle_data contains 6 items
        #if not, raise error and skip that line
        try:
             if len(vehicle_data) != 6:
                raise Exception(f"There is an error in your data file on line {line_number}")
        except Exception as error:
            print(str(error))
            continue

        #get individual values from the resulting list
        try:
            make = vehicle_data[0]
            model = vehicle_data[1]
            vin = vehicle_data[2]
            if vehicle_data[3].lower() == "electric":
                engine_size = 0
            else:
                engine_size = float(vehicle_data[3])
            owner = vehicle_data[4]
            year = int(vehicle_data[5])
        except Exception as error:
            print(f"Error: {error} on line {line_number}")
            continue

        #create automobile objects with the data
        new_auto = Auto.Automobiles(make,model,vin,engine_size,owner,year)

        #append each automobile to the list
        auto_list.append(new_auto)
    file.close()
    return auto_list

def main():
    #load a list of automobiles from data in a file
    automobile_list = load_vehicles("vehicle_data.csv")

    #print info for each automobile in a for loop
    for vehicle in automobile_list:
        vehicle.print_info()

main()