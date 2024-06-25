import Student
import random
from datetime import datetime
"""
Function to write error log file
Input: error message
Output: none
"""
def write_to_error_log(error_message):
    try:
        #open log file
        log_file = open("error_log.txt", "w")
        #write error message to log file
        log_file.write(f"{datetime.now()}: {error_message}\n")
        #close log file
        log_file.close()
    except Exception as err:
        print(err)
    
    return

def load_students(file_name):
    student_list = []

    #open the file
    file = open(file_name, "r")

    #ignore the header in the file
    file.readline()

    #read each line of the file in a for loop
    line_number = 1
    for line in file:
        line_number += 1

        #split the lines at the commas
        student_data = line.split(",")

        #check that student_data contains 6 items
        #if not, raise error and skip that line
        try:
             if len(student_data) != 6:
                raise Exception(f"There is an error in your data file on line {line_number}")
        except Exception as error:
            write_to_error_log(str(error))
            continue

        #get individual values from the resulting list
        try:
            f_name = student_data[0]
            l_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
            id = int(student_data[5])
        except Exception as error:
            write_to_error_log(f"Error: {error} on line {line_number}")
            continue

        #create student objects with the data
        new_student = Student.Students(f_name,l_name,major,credit_hours,gpa,id)

        #append each student to the list
        student_list.append(new_student)
    file.close()
    return student_list

#create a function called student_to_dictionary that creates a student dictionary for each student object
#add student dictionaries to a list
#function to create a list of student dictionaries
def student_to_dictionary(student, student_dictionary_list):
    student_dictionary = {
        "f_name": student.get_f_name(),
        "l_name": student.get_l_name(),
        "major": student.get_major(),
        "gpa": student.get_gpa(),
        "class": student.get_class_level(),
        "id": student.get_id()
    }
    student_dictionary_list.append(student_dictionary)
    
def get_student_dictionaries():
    students_list = load_students("students.csv")
    student_dictionary_list = []
    for student in students_list:
        student_dictionaries = student_to_dictionary(student, student_dictionary_list)
    return student_dictionary_list