# Asking for amount of students
amount_students = int(input("Enter the amount of students are registering\n:"))

# Creating the reg form
with open("reg_form.txt", "w+") as f:
    # Keeps asking for id num for the amount of students
    for _ in range(amount_students):
        id_num = input("Enter id number: ")
        # Writing id to file with each loop
        f.write(f"ID: {id_num} \n")
