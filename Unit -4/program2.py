def student_record():
    name=input("Enter student name: ")
    roll_no=input("Enter student roll number: ")
    marks=input("Enter student marks: ")
    print("Student Record:")
def display_record():
    try:
        with open("student_record.txt", "r") as file:
            records = file.readlines()
            if len(records) == 0:
                print("No records found.")
            else:
                print("Student Records:")
                for record in records:
                    roll_no, name, marks = record.strip().split(",")
                    print("Roll Number:", roll_no)
                    print("Name:", name)
                    print("Marks:", marks)
                    print()
    except FileNotFoundError:
        print("No records found. The file does not exist.")
