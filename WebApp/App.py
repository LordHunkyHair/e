#import modules
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a flask app
app = Flask(__name__)
app.config["DEBUG"] = True

#set a secret key to use when validating form data
app.config["SECRET_KEY"] = "your secret key"

#define a constant value for url
URL = "http://127.0.0.1:5000/api/students/all"

#function to request student data from the api
def get_student_data(URL):
    #make a request
    response = requests.get(URL)

    #convert format to json
    response_json = response.json()

    return response_json

#function to return unique majors
def get_majors():
    #get a list of students from the student api
    student_list = get_student_data(URL)

    #produce a list of unique majors
    unique_majors = []
    for student in student_list:
        if student["major"] not in unique_majors:
            unique_majors.append(student["major"])
    unique_majors.sort()
    return unique_majors

#create a route for the site index page that will display all student data
@app.route("/", methods=['GET'])
def index():
    #get the student data
    student_data = get_student_data(URL)

    #send the student data to the index.html page
    return render_template('index.html', student_data=student_data)

@app.route('/majors', methods=['GET'])
def majors():
    #write code thyat gets a unique list of majors from student data
    major_list = get_majors()
    #get student data from the api: list of student dictionaries


    return render_template('majors.html', major_list=major_list)

@app.route('/majors', methods=['POST'])
def majors_post():
    major_list = get_majors()
    result_list = []

    #get form data
    major = request.form.get('major')

    #validate form data. if invalid, show error message
    if not major:
        flash("You must select a major")
    else:
    #find students with the selected major and return to the majors.html page
    #get student data
        URL = "http://127.0.0.1:5000/api/students/all"
        student_list = get_student_data(URL)

        #loop through list of students. if student major is equal to major, place student in a result list
        for student in student_list:
            if student["major"] == major:
                result_list.append(student)
        
        #send the result list to the majors.html page

    return render_template('majors.html', major_list=major_list, result_list=result_list)

app.run(port=5005)