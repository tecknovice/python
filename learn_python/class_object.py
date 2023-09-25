from student import Student

student1 = Student("Hung", "Computer Engineering", 2.85, False)
print(student1)

student2 = Student("Kevin", "Machine learning and Data Science", 3.5, True)
print(student2)


print(student1.on_honor_roll())
print(student2.on_honor_roll())