def main():
    scores = [1, 4, 6, 7, 78]
    students = ["Alice", "Henry", "Tom", "Joey", "Audrey"]
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")
    
    #create a dictionary of names and scores
    print()
    student_scores = {
        "Alice": 87,
        "Henry": 79,
        "Tom": 94,
        "Audrey": 90
    }
    print(student_scores["Audrey"])
    print(student_scores["Tom"])

    #get all keys and values from the student score dictionary
    print()
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

    #declare a car dictionary
    car = {"make": "Ferarri", "model": "F-50", "year": 2021, "value": 500000, "engine": 4.8}

    #get all keys and values from the car dictionary
    print()
    for key, value in car.items():
        print(f"{key}: {value}")

main()