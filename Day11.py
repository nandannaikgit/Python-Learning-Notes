# l = [1,23,45,66,78]
# sum=0
# for num in l:
#     sum=sum+num
# print(sum)


# l = [1,23,45,66,78]
# dl=[]
# for num in l:
#     dl.append(num*2)
#     print(dl)


# student_marks = {"nandan":99,"pradeep":89,"divakar":90}
# for student, marks in student_marks.items():
#     print(f"{student}---{marks}")

# students = ["nandan","darshan","divakar"]
# marks = [25,45,68]
# students_marks = {}
# for index, student in enumerate(students):
#     students_marks[student] = marks[index]
# print(students_marks)


# students = ["nandan","darshan","divakar"]
# marks = [25,45,68]
# students_marks = {}
# for i in range(0,len(students)):
#     students_marks[students[i]] = marks[i]
# print(students_marks)

#list comprehension
# l=[1,2,3,4,5]
# dl=[item*2 for item in l]
# print(dl)

# l=[1,2,3,4,5]
# print(l)
# dl=[item*2 for item in l if item%2==0]
# print(dl)

# l=["hajsjxh","ajadhss","ashjxh"]
# print(l)
# cl=[x[1] for x in l]
# print(cl)


#dictionary comprehension
# names = {"nandan":99,"pradeep":89,"divakar":90}
# d={name:len(name) for name in names}
# print(d)

# cities={
#     "bengaluru":22,
#     "mangaluru":34,
#     "bhatkal":22,
#     "byndoor":12
    
# }
# lc={key:value for key,value in cities.items() if value>20}
# print(lc)

# s = "this is a computer"

# l = s.split()
# print(l)


# x=input("Enter list of integers: ").split()
# l=[int(num) for num in x]
# print(l)

#or
l=[int(num) for num in input("Enter list of integers: ").split()]
print(l)