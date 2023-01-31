import csv

infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")

next(infile)

customer_sales_report = csv.reader(infile, delimiter=",")

outfile.write("Customer ID  |  Total\n")

Customer_ID = "250"
Customer_Total = 0

for item in customer_sales_report:
    if Customer_ID != item[0]:

        outfile.write(
            Customer_ID + "             " + str("%.2f" % Customer_Total) + "\n"
        )

        Customer_ID = item[0]
        Customer_Total = 0

    Total = float(item[3]) + float(item[4]) + float(item[5])
    Customer_Total += Total

outfile.write("261" + "             " + str("%.2f" % Customer_Total))

infile.close()
outfile.close()
