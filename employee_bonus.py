import csv

infile = open("EmployeePay.csv", "r")
csvreader = csv.reader(infile, delimiter=",")
next(csvreader)

for item in csvreader:

    total = float(item[3]) + (float(item[3]) * float(item[4]))

    print()
    print("Employee ID: ", item[0])
    print("First Name:  ", item[1])
    print("Last Name:   ", item[2])
    print("Base Salary: ", item[3])
    print("Bonus:       ", item[4])
    print("Total:       ", total)
    print()

    input()

infile.close()
