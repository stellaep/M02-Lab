"""Name: Stella Plahitko
   File name: M02_Lab.py
   Description: This app prompts the user to input a student's first name, last name, and gpa.
                It will then output a message stating whether the student is on the dean's list,
                honor roll, or neither."""
last_name = str(input("Enter the student's last name: "))
while last_name != "ZZZ":
    first_name = str(input("Enter the student's first name: "))
    gpa = float(input("Enter the student's GPA: "))
    if gpa < 3.25:
        print(first_name, last_name, " is not on the dean's list or honor roll.")
    elif gpa < 3.5:
        print(first_name, last_name, " is on the honor roll.")
    else:
        print(first_name, last_name, " is on the dean's list.")
    last_name = str(input("Enter the student's last name: "))