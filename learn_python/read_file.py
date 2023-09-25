# open("employees.txt", "r") read
# open("employees.txt", "r+")  # reading and writing

employee_file = open("employees.txt", "r")
print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)
employee_file.close()  # close it at the end
