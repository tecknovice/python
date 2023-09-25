# open("employees.txt", "w") overwrite the file
# open("employees.txt", "a")  # append to the end of the file
employee_file = open("employees.txt", "a")  # append to the file
employee_file.write("\nJean - Human Resources")
employee_file.write("\nKelly - Customer Service")
employee_file.close()  # always close file at the end

web_page = open("index.html", "w")
web_page.write("<h1>This is a header</h1>")
web_page.close()
