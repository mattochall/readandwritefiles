import csv

customers = open("customers.csv", "r")
customers_country = open("customer_country.csv", "w")

customer_file = csv.reader(customers, delimiter=",")

for item in customer_file:
    customers_country.write(item[1] + " " + item[2] + ", " + item[4] + "\n")

customers.close()
customers_country.close()
