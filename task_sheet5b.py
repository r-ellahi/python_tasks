#CSV

# Q1 read the ford_escort.csv example file using python csv library and print each row 
import csv 
with open('ford_escort.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        print(row)


# Q2 Extend the above so that the data is read into a dictionary 
import csv 
with open('ford_escort.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row)


# Q3. Write the following data as CSV to a file. Adde a header row with titles.
['Joe', 'Bloggs', 40]
['Jane', 'Smith', 50]

import csv
with open('trial.csv', mode = 'w') as file:
    writer = csv.writer(file, delimiter = ',')
    writer.writerow(['First', 'Surname', 'Age'])
    writer.writerow(['Joe', 'Bloggs', '40'])
    writer.writerow(['Jane', 'Smith', '50'])


# Q4. Write another block of code that will append the following data to the file created in Q3
['Mike', 'Wazowski', 40]

import csv
with open('trial.csv', 'a') as file:
    writer = csv.writer(file, delimiter = ',')
    writer.writerow(['Mike', 'Wazowski', '40'])

#EXTRA WORK - WRITING FROM A DICTIONARY 
import csv

with open('dictionary.csv', 'w') as file:
    fieldnames = ['first_name', 'surname', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
    'first_name': 'Jack',
    'surname': 'Smith',
    'age': 25
})


#JSON
# Q1: read the example.json handout file using the native python json library,
# print the object that is created

import json
with open('example.json', 'r') as json_file:
    data = json.load(json_file)
    print(json.dumps(data, indent =3))
# indent allows for spacing in between values



# Q2: print the "id" of all the items in the menu
import json
with open('example.json', 'r') as json_file:
    data = json.load(json_file)
    print(json.dumps(data['menu']['items'], indent =3))



# #Q3 Write the following data as JSON to a file
import json
data = {
    'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}

with open('data_file.json', 'w') as write_file:
    json.dump(data, write_file)
