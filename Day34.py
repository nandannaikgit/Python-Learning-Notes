"""File Handling"""

file = open("notes.txt","r")
content = file.readlines()
print(content)
file.close()

