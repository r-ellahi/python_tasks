# LOOPS

for x in range(0, 11):
     print(x)

y = 0
while y < 11:
    print(y)
    y += 1


nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
for nums in nums:
    print(nums)



for x in range(0, 11):
     print(x)
else:
    print("Done!")


list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]
for x in list1:
    for y in list2:
        if x==y:
            print(x)


import random
x = random.randint(1,100)

while True:
    x = random.randint(1, 100)
    if x % 5 == 0:
        print('multiple of 5: stopping loop')
        break
    elif x % 3 == 0:
        print('multiple of 3: skipping iteration')
    continue
else:
    print(x)
 
 
# DICTIONAIRY 
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year' : 1964,
    'colour': 'Yellow'
}
x = car.items()
print(car)

for key, value in car.items():
  print("key: " + key + ", value: " + str(value))


# ARGS AND KWARGS
def my_try(*people):
    for person in people:
        print(person)
my_try('is', 'this', 'right')


def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
        print(result)
concatenate(a="Real", b="Python", c="Is", d="Great", e="!")


# Functions
def add_numbers(a, b):
    return a + b
result = add_numbers(1, 2) 
print(result)


def add_numbers(*nums):
    result = 0
    for num in nums:
        result += num
        return result
result = add_numbers(1, 2, 3, 4)
print(result)

def two_numbers(**kwargs):
    sum = {}
    for key, value in kwargs.items():
        sum[key] = value
    return(sum)

numbers = [ ]
x = two_numbers(number = 32, number2 = 34, number3 = 43)
print(x)



# Create a scientific/basic calculator that makes use of separate functions to perform calculations, such as: add , divide , area_of_a_circle etc...

def add(x, y):
    return x + y

#This function subtracts two numbers
def subtract(x, y):
    return x - y

# #This function multiplies two numbers
def multiply(x, y):
    return x * y

# #This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    #Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

   #Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, '=', divide(num1, num2))

