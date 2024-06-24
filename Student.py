class Students():

    #define a student constructor
    def __init__(self, f_name, l_name, major, credit_hours, gpa, id):
        #assign class properties values
        self.__f_name = f_name
        self.__l_name = l_name
        self.__major = major
        self.__credit_hours = int(credit_hours)
        self.__gpa = float(gpa)
        self.__id = int(id)

    #create get and set methods for class properties
    def get_f_name(self):
        return self.__f_name
    
    def get_l_name(self):
        return self.__l_name
    
    def get_major(self):
        return self.__major
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, new_credit_hours):
        #check that new_hours is not a negative or a string
        if type(new_credit_hours) == str or type(new_credit_hours) == float or new_credit_hours < 0:
            print("Error: Credit Hours must be a positive integer")
            return
        self.__credit_hours = new_credit_hours
    
    def get_gpa(self):
        return self.__gpa

    def get_id(self):
        return self.__id
    
    def get_class_level(self):
        if self.__credit_hours > 0 and self.__credit_hours <= 30:
            self.class_level = "Freshman"
        if self.__credit_hours > 30 and self.__credit_hours <= 60:
            self.class_level = "Sophomore"
        if self.__credit_hours > 60 and self.__credit_hours <= 90:
            self.class_level = "Junior"
        if self.__credit_hours > 90:
            self.class_level = "Senior"
        return self.class_level

    def print_student_data(self):
        print(f"{self.__f_name} {self.__l_name} {self.__major}")
        print(f"Credit Hours: {self.__credit_hours}, GPA: {self.__gpa}")
        print(f"ID: {self.__id}\n")