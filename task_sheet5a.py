# Q1 - create a CSV file with whatever data - read the file and print each row

import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)


# Q2 - extend the above so that the data is read into a dictionary 
import csv
with open("data.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row)


# Q4 - extend the data by writing another block of code that will append to the file
import csv
with open('data.csv', 'a') as file:
    writer = csv.writer(file, delimiter = ',')
    writer.writerow(['lana', '37', '1.45'])
