def main():

    a = 7
    b = 7
    if a > b:
        print(f"{a} is greater than {b}")
    elif a < b:
        print(f"{a} is less than {b}")
    else:
        print(f"{a} is equal to {b}")
    
    #print the appropriate letter grade based on the test score
    test_score = float(input("Please enter your test score: "))
    if test_score >= 90:
        if test_score >= 97:
            print(f"{test_score} --> A+")
        if 97 > test_score >= 93:
            print(f"{test_score} --> A")
        if 93 > test_score >= 90:
            print(f"{test_score} --> A-")
    elif 90 > test_score >= 80:
        if test_score >= 87:
            print(f"{test_score} --> B+")
        if 87 > test_score >= 83:
            print(f"{test_score} --> B")
        if 83 > test_score >= 80:
            print(f"{test_score} --> B-")
    elif 80 > test_score >= 70:
        if test_score >= 77:
            print(f"{test_score} --> C+")
        if 77 > test_score >= 73:
            print(f"{test_score} --> C")
        if 73 > test_score >= 70:
            print(f"{test_score} --> C-")
    elif 70 > test_score >= 60:
        if test_score >= 67:
            print(f"{test_score} --> D+")
        if 67 > test_score >= 63:
            print(f"{test_score} --> D")
        if 63 > test_score >= 60:
            print(f"{test_score} --> D-")
    else:
        print(f"{test_score} --> F")

    #grade decision restructured
    print("\nGrade Decision: 2")
    test_score = float(input("Please enter your test score: "))
    if test_score >= 90:
        if test_score >= 97:
            print(f"{test_score} --> A+")
        elif test_score >= 93:
            print(f"{test_score} --> A")
        elif test_score >= 90:
            print(f"{test_score} --> A-")
    elif test_score >= 80:
        if test_score >= 87:
            print(f"{test_score} --> B+")
        elif test_score >= 83:
            print(f"{test_score} --> B")
        elif test_score >= 80:
            print(f"{test_score} --> B-")
    elif test_score >= 70:
        if test_score >= 77:
            print(f"{test_score} --> C+")
        elif test_score >= 73:
            print(f"{test_score} --> C")
        elif test_score >= 70:
            print(f"{test_score} --> C-")
    elif test_score >= 60:
        if test_score >= 67:
            print(f"{test_score} --> D+")
        elif test_score >= 63:
            print(f"{test_score} --> D")
        elif test_score >= 60:
            print(f"{test_score} --> D-")
    else:
        print(f"{test_score} --> F")

main()