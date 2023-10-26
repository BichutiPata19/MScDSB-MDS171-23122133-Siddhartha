# Create a menu driven program that collects students details
# > Name
# > Email
# > Phone
# [Use dictionary to store student details]

# Menu Options 
# 1. Create Students
# 2. Search for Students
# 3. Print Students

# Initialize an empty dictionary to store student details
student_details = {}

# Function to create a new student entry
def create_student():
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    phone = input("Enter student phone: ")
    student_details[name] = {"Email": email, "Phone": phone}
    print(f"{name}'s details have been added.")

# Function to search for a student by name
def search_student():
    name = input("Enter student name to search: ")
    if name in student_details:
        print(f"Student Name: {name}")
        print(f"Email: {student_details[name]['Email']}")
        print(f"Phone: {student_details[name]['Phone']}")
    else:
        print(f"{name} not found in the database.")

# Function to print all student details
def print_students():
    if not student_details:
        print("No student records found.")
    else:
        print("Student Details:")
        for name, details in student_details.items():
            print(f"Name: {name}")
            print(f"Email: {details['Email']}")
            print(f"Phone: {details['Phone']}")
            print("-" * 20)

# Menu loop
while True:
    print("\nMenu Options:")
    print("1. Create Students")
    print("2. Search for Students")
    print("3. Print Students")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        create_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        print_students()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
