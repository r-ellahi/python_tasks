# #Strings
first_name = "john"
surname = "doe"
print("Hi, my name is" + first_name + " " + surname )


#Integers
x = 5
y = 10
z = x * y
print(z)
print(f'the product of {x} and {y} is {z}')


#Lists
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
third_element = people[2]
print(third_element)

fifth_element = people[-3]
print(fifth_element)

new_list = people[2:-1]
print(new_list)

newnew_list = people[0:1]
print(newnew_list)

print('first element in people array is equal to last element: ', people[0] == people[-1])


# Input
x = input('What is your name?')
print("Hi, " +  x)

num1 = int(input('Pick a number'))
num2 = int(input('Pick another number, '))
print(f'so {num1} multiplied by {num2} equals {num1 * num2}')

num1 = int(input('Pick a number'))
num2 = int(input('Pick another number, '))
if num1 == num2:
    print(True)
else:
    print(False)



# Part 2

num = int(input('Pick a number'))
if num % 2 == 0:
    print('thats pretty even')
else:
    print('thats odd')

num = int(input('Pick a number'))
if num % 4 == 0:
    print('thats pretty even')
else:
    print('thats odd')


num = int(input('Pick a number'))
if num % 15 == 0:
    print('fizzbuzz')
elif num % 5 == 0:
    print('buzz')
elif num % 3 == 0:
    print('fizz')
else:
    print('invalid answer')
# remember python execute in order 
# if %3 / %5 is before %15 then answer will always be fizz OR buzz


# Part 3
choice = input("Convert to Celsius(s) or Faranehit(f)")
temperature = int(input("Please eneter the temperature to convert: "))

if choice == "c":
    converted_temperature = (temperature - 32) * (5/9)
    print(converted_temperature)
elif choice == "f":
    converted_temp2 = (temperature * 1.8) + 32
    print(converted_temp2)
else:
    print("Input not understood")


# Part 4
age = int(input("How old are you?"))
salary = int(input("How much do you earn?"))
if age > 29 and salary >= 50000:
    print("I can offer you a loan of up to £100,000!")
elif age > 29 and salary >= 75000:
    print("I can offer you a loan of up to £75,000!")
elif age > 20 and salary >= 21000:
    print("I can offer you a loan of up to £50,000!")
else:
    print("Sorry you are not eligable for a loan")