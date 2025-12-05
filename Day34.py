"""File Handling"""

# file = open("notes.txt","r")
# content = file.readlines()
# print(content)
# file.close()

# file = open("student.txt","w")
# file.write("nandan\n")
# file.write("djfhdfvhjv")
# file.close()


# file = open("student.txt","a")
# file.write("nandan\n")
# file.write("djfhdfvhjv\n")
# file.close()

# file = None
# try:
#     file = open("student.txt","x")
#     file.write("nandan\n")
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     if file:
#         file.close()


# students = ["nandan","pradeep", "divakar"]

# file = open("class.txt", "w")

# for student in students:
#     file.write(f"{student}\n")
    
# file.close()


# students = ["nandan","pradeep", "divakar"]

# with open("class2.txt", "w") as file:
#     for student in students:
#         file.write(f"{student}\n")

with open("student.txt", "r") as file:
    for line in file:
        print("Student:", line.strip())