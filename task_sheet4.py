#  Q1 Use the below list to write all names to a file where each name is on a new line
people = ['John', 'Sally', 'Mark', 'Lisa', 'Joe', 'Barry', 'Jane']

file = open('people.txt', 'w')
for person in people:
    file.write(person + '\n')
file.close()


# Q2 Extend this to use try-catch
people = ['John', 'Sally', 'Mark', 'Lisa', 'Joe', 'Barry', 'Jane']
try:
    file = open('people.txt', 'w')
    for person in people:
        file.write(person + '\n')
        file.close()
except Exception as e:
    print('An error occurred: ' + str(e))



# Q3 Extend this to use try-catch-finally.
people = ['John', 'Sally', 'Mark', 'Lisa', 'Joe', 'Barry', 'Jane']
file = None
file = open('people.txt', 'w')
for person in people:
    file.write(person + '\n')

except Exception as e:
    print('An error occurred: ' + str(e))
    finally:
    file.close()



# Q4 Extend this to make use of the file context manager. 

try:
    with open('people.txt', 'w') as file:
        for person in people:
            file.write(person + '\n')
        except Exception as e:
            print('An error occurred: ' + str(e))
