import csv

infile = open("EmployeePay.csv", "r")
csvreader = csv.reader(infile, delimiter=",")

for record in csvreader:
    print()
    print("Employee ID: ", record[0])
    print("First Name: ", record[1])
    print("Last Name: ", record[2])
    print("Base Salary: ", record[3])
    print("Bonus: ", record[4])
    print()

infile.close()
