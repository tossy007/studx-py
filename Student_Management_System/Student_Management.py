                                    # Student Record System
import json
import random
import os

# Adding Student in a Dictionary
def add_students(info):
    no = int(input("Enter number of students: "))
    for i in range(no):
        name = input("Enter Students Name: ")
        Age = input("Enter age : ")
        code = random.randint(1000, 9999)
        while (
            str(code) in info
        ):  # <!!!This makes the random combination for student id /Identification id,
            code = random.randint(
                1000, 9999
            )  # To identify whether is a student is Genuine!!!>
        student_data = {"Name": name, "age": Age}
        info[str(code)] = student_data
    for ide, data in info.items():
        print(
            f"Student ID : {ide} || Student Name :{data['Name']} || Student Age :{data['age']}"
        )
    print("\n")
    return info

# Delete function from the main Data / Dictionary
def delete_student(info):
    print("\n")
    x = input("Enter Your Student Id : ")
    if x in info:
        info.pop(x)
        print("Deleted successfully !!")
        return info
    else:
        print("Student Not Found -'404'- ")

# Updating the main Data / Dictionary
def Update_student(info):
    select = input("Enter the student id :")
    if select in info:
        print("Enter Changes Needed in : \n")
        print("1) Name")
        print("2) Age ")
        changes = int(input("Enter The no: "))
        if changes == 1:
            new_name = input("Enter the new name :")
            info[select]["Name"] = new_name
            print("Updated Successfully !!!")
        elif changes == 2:
            new_age = input("Enter your new age :")
            info[select]["age"] = new_age
            print("Updated Successfully !!!")
        else:
            print("Enter valid choice !!!")
    else:
        print("No record found !!")
    return info

# Displaying the Data
def display_student(info):
    print("\n")
    print(":: Student Record ::")
    for i, v in info.items():
        print(f" => details {v}")
    print("\n")
    return info

# This function saves the data in the memory
def save_file(info):
    file_path = os.path.join(os.path.dirname(__file__), "Student.json")
    with open(file_path, "w") as f:
        json.dump(info, f)

# This function loads the saved data!
def load_file():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "Student.json")
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

data = load_file()
while True:
    print("1)Add student")
    print("2)Delete student")
    print("3)Update student info")
    print("4)View all students")
    print("5)Exit")

    choice = int(input("Enter your choice :"))

    if choice == 1:
        data = add_students(data)
        save_file(data)
    elif choice == 2:
        data = delete_student(data)
        save_file(data)
    elif choice == 3:
        data = Update_student(data)
        save_file(data)
    elif choice == 4:
        display_student(data)
    elif choice == 5:
        break
    else:
        print("Enter valid choice :")