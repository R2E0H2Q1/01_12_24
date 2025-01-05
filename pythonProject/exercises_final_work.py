# Python Basic - Final Work
# Ex 1:Write a for loop that prints the numbers from 12 to 24.

print(f'Ex.1. List of numbers from 12 to 24: ', end=' ')
for i in range(12, 25):
    print(i, end=' ')
print()
# Ex 2: Write a for loop that prints the ODD numbers from 7 to 31

print(f'Ex.2. List of odd numbers: ', end=' ')
for i in range(7, 32, 2): # adding the 2 will skip over the even numbers
        print(i, end=' ')
print()

# Ex 3: Write a for loop that prints the EVEN numbers from 10 to -20.

print(f'Ex.3. List of even numbers: ', end=' ')
for i in range(10, -21, -2):
        print(i, end=' ')
print()

"""Ex 4: Write a for loop that iterates through all numbers from 1 to 45. Print the following:
● For each number that multiples of 3 print “Fizz”
● For each number that multiples of 5 print “Buzz”
● For each number that multiples of 3 and 5 print “FizzBuzz”"""

print(f'Ex.4. List of numbers from 1 to 45: ', end= '')
for num in range(1, 46):
    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} - FizzBuzz | ', end= '')
    elif num % 3 == 0:
        print(f'{num} - Fizz | ', end= '')
    elif num % 5 == 0:
        print(f'{num} - Buzz | ', end= '')
    else:
        print(f'{num} - No relevant | ', end= '')
print()

"""Ex 5: Write a function that receives an array as a parameter and calculates the sum of all the numbers in the given array 
(don’t use sum() function). For example if the given array is: [1,13,22,123,49,34,5,24,57,45] The result should be 373"""

def array_sum(num_list):
#    return sum([num for num in num_list]) #comprehension using sum()

    total = 0
    for num in num_list:
        total += num
    return total

example = [1,13,22,123,49,34,5,24,57,45]
total = array_sum(example)
print(f'5. The total for the sum of {example} is {total}: ')
print()

"""Ex 6: Write a function that receives a list of objects. Each object should represent a student with the properties:
● id
● first name
● last name
● age
● country
● city

In addition, the function should receive a property to change.
1 - The function should check for each property in each object in the array if the given property exists and if it does,
the function should delete it from the object.
2 - Write a function that prints each property of each object in the given array.
3 - Write a function that sorts the array by the students age from the oldest to the youngest and return the sorted list"""

def removal(students, city): #1. checkfor an object on the list and if present on the list remove it.
    for student in students:
        if city in student:
            del student[city]
    return students


def applicant_students(students): #to print all students properties
    for student in students:
        print("Student ID: " + str(student.get("id")) + ", " +
              "First Name: " + str(student.get("first_name")) + ", " +
              "Last Name: " + str(student.get("last_name")) + ", " +
              "Age: " + str(student.get("age")) + ", " +
              "Country: " + str(student.get("country")) + ", " +
              "City: " + str(student.get("city")))

def sorted_age(students):
    return sorted(students, key=lambda _: _.get('age', 0), reverse=True)

students = [
    {"id": 1, "first_name": "Alice", "last_name": "Smith", "age": 25, "country": "USA", "city": "New York"},
    {"id": 2, "first_name": "Bob", "last_name": "Johnson", "age": 20, "country": "Canada", "city": "Toronto"},
    {"id": 3, "first_name": "Charlie", "last_name": "Davis", "age": 22, "country": "UK", "city": "London"},
    {"id": 4, "first_name": "David", "last_name": "Williams", "age": 28, "country": "Australia", "city": "Sydney"}
]

students = removal(students, "city")

print('Student properties after removal of city:')
applicant_students(students)

sorted_list = sorted_age(students)
print()
print(f'The list after sorted by age from the oldest to youngest is:')
applicant_students(sorted_list)
print()

#Ex 7:

our_pets = [
    {
        "animal_type": "cat",
"names": [
"Meowzer",
"Fluffy",
"Kit-Cat"
]
},
{
"animal_type": "dog",
"names": [
"Spot",
"Bowser",
"Frankie"
]
}
]

#7.1 - Write a function that receives the list shown above and prints only animalType: cat.

def cat_details(our_pets):
    for cat_pet in our_pets:
        if cat_pet["animal_type"] == "cat":
            print(f' 7.1. The animal type is: {cat_pet}')

cat_details(our_pets)

#7.2 - Write a function that receives the list shown above and the animal type. The function should print all names of that animal type if
# this type exists in the object.


def double_check(our_pets, animal_type):
    check_up = False
    for check_pet in our_pets:
        if check_pet["animal_type"] == animal_type:
            check_up = True
            print(f' 7.2. The names of the animals are: {check_pet["names"]}')

    if not check_up:
        print(f'7.2. No pets of type {animal_type} found.')

double_check(our_pets, "dog")

# 3 - Write a function that that receives the list shown above and animal name. The function should add the specified animal name to each
# ‘names’ list in each animal_type if that name does not exist in the ‘names’ list.

# Ex 8:
student = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}
# 8.1 - Write a function that prints all the student data (each student property should be printed in a new line).

def student_details(student):
    for key, value in student.items():
        print(f'8.1. {key}: {value}')

student_details(student)

# 2 - Write a function that receives the student object and a hobby, the function should add the hobby to the student's hobbies list
# if it’s not exist already.

def hobbies(student, hobby):
    if hobby in student['hobbies']:
        print(f' 8.2. The hobby {hobby} already exist on the list')

    else:
        student['hobbies'].append(hobby)
        print(f'8.2.{hobby} was added to list of hobbies!')

hobbies(student, 'fishing')

# 8.3 - Use the function that you wrote in ex 1 to print the data of the student and check that the new hobby has been added.

def student_details(student):
    for key, value in student.items():
        print(f'8.3. {key}: {value}')

student_details(student)

# 4 - Write a function that receives an object of a student and hobby, the function should delete the hobby from the student's hobbies.

def delete_hobby(student, hobby):
    if hobby in student['hobbies']:
        student['hobbies'].remove(hobby)
        print(f'8.4. The hobby {hobby} was deleted from the list!')
    else:
        print(f'8.4. Hobby {hobby} is not present on the list!')

delete_hobby(student, 'games')

# 5 - Use the function that you wrote in ex 1 to print the data student and check that the hobby has been deleted from the object student.

def student_details(student):
    for key, value in student.items():
        print(f'8.5. {key}: {value}')

student_details(student)

# 6 - Add to the object student new property: family_name and add a value.

def add_lastname(student, last_name):
    student['last_name'] = last_name
    print(f'8.6. Last name {last_name} was added to the student list!')

add_lastname(student, 'Levi')

def student_details(student):
    for key, value in student.items():
        print(f'8.6. {key}: {value}')

student_details(student)

# Ex 9: Write a function that prints all the elements of a second list using nested for loops.

matrix = [
 [1, 2],
 [3, 4],
 [5, 6]
]
# print_matrix(matrix) → Should print: 1 2 3 4 5 6

print(f'9. The list of nested loops is: ', end=' ')
def nested_loop_print(matrix):
    for row in matrix:
        for num in row:
            print(f'{num}', end=' ')

nested_loop_print(matrix)
print()
# Ex 10: Write a function to count how many zeros appear in a 2D matrix, using nested for loops and increment operation.
matrix_2d = [
 [0,1,1],
 [0,1,0],
 [1,0,0]
];
# print(zero_count(matrix)) → Should print: 5

def zero_count(matrix):

    count = 0

    for row in matrix:
        for value in row:
            if value == 0:
                count += 1
    return count

print(f'10. Zero appears {zero_count(matrix_2d)} times in {matrix_2d}')

# Ex 11: Write a function to return a list of all the elements that are repeated more than once in a given list.
# list = [4,2,34,4,1,12,1,4]
# print(find_dup(list)) Should print: [4, 1]

def find_dup(num_list):
    checked = set()
    duplicates = []

    for num in num_list:
        if num in checked:
            if num not in duplicates:
                duplicates.append(num)
        else:
            checked.add(num)
    return duplicates

list = [4, 2, 34, 4, 1, 12, 1, 4]
print(f'11. The duplicated numbers on {list} are: {find_dup(list)}')

# Ex 12: Write a function using a for loop that gets a list and returns a new list with the elements from the given list
# appearing in reverse order. (Don’t use list reverse() method)
# For example:
# list = [43, "what", 9, true, "cannot", false, "be", 3, true];
# Function output should be:
# [true, 3, “be”, false, “cannot”, true, 9, “what”, 43]

def reverse_order(my_list):
    reversed_list = []
    for object in my_list:
        reversed_list.insert(0, object)
    return reversed_list

first_list = [43, "what", 9, True, "cannot", False, "be", 3, True];
print(f'12. Reversed list: {reverse_order(first_list)}')

# Ex 13: Given two list as integers. Add up each element in the same position and create a new list containing the sum
# of each pair. Assume both list are of the same length. For example:
# first_array = [4, 6, 7];
# second_array = [8, 1, 9];
# Function output should be: [12, 7, 16]

def concatenated_list(list_one, list_two):
    if len(list_one) != len(list_two): #checks if both lists are the same size.
        return 'Both lists must be of an equal length!'

    conct_list = []
    for num in range(len(list_one)):
        conct_list.append(list_one[num] + list_two[num])

    return conct_list

list_one = [4, 6, 7];
list_two = [8, 1, 9];
print(f'13. Concatenated list: {concatenated_list(list_one, list_two)}')

# Ex 14: Write a program that will check if two strings are palindromes. A palindrome is a word that spells the same
# forward and backward. Palindrome: a word, phrase, or sequence that reads the same backward as forward, examples
# for valid palindromes: madam, nurses run. For example:
# first_str = "racecar"
# second_str = "Java"
# Function output should be:
# True (for first_str)
# False (for second_str)

import string

def palindrome_check(string_example):
    string_example = string_example.lower() #To make everything lowercase and avoid comparison issues.
    string_example = ' '.join(pali for pali in string_example if pali.isalnum()) #Removes non alphanumeric characters.
    return string_example == string_example[::-1] #checks if the string is the same backwards and forward

first_str = "racecar"
second_str = "Java"
print(f'14.1. Is {first_str} a Palindrome? {(palindrome_check(first_str))}')
print(f'14.2. Is {second_str} a Palindrome? {(palindrome_check(second_str))}')

# Ex 15: Write a while loop that iterates as long as the counter is less than 100, on every iteration the counter is multiplied
# by 2 starting from 1.

def less_than_100(number):
    count = number #This way will start with the provided number
    while count < 100:
        count *= 2 #will multiply by 2 on every iteration
    return count #Returns the last value while counter was < 100.
print(f'15. The counter has reached {less_than_100(1)}')

# Ex 16: Write a while loop that iterates as long as the counter is greater than 50 , on every iteration the counter is divided
# by 2. The counter should start with the value 900000 before the first iteration.

def greater_than_50(value):
    count = value #This way will start with the provided number
    while count > 50:
        count /= 2 #will divided by 2 on every iteration
    return count #Returns the last value while counter was < 100.
print(f'16. The counter has reached {greater_than_50(900000)}')

# Ex 17: Write a function that gets a list of strings as parameter and returns a new array containing all the values
# that appear more than once. In your solution. Use only while loops.

def check_duplicates_list(list_strings):
    duplicates = []
    value = 0
    while value < len(list_strings):
        if list_strings.count(list_strings[value]) > 1 and list_strings[value] not in duplicates:
            duplicates.append(list_strings[value])
        value += 1
    return duplicates

test_list = ["Toyota", "Ford", "BMW", "Honda", "Chevrolet", "Toyota", "Audi", "BMW", "Mercedes", "Ford", "Chevrolet", \
             "Hyundai", "Nissan", "Tesla", "BMW", "Toyota", "Nissan", "Subaru", "Honda", "Ford"]
print(f'17. The duplicated values are: {check_duplicates_list(test_list)}')

# Ex 18: Write a function that gets an array of strings as parameter and returns a new list containing all the values from the
# provided array in the same order but without any duplicated values. In your solution use only while loops.
# For example:
# names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', ‘Chris’, ‘Kevin’]
# Function output should be: ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor']

def no_duplicates(list_no_duplicates):
    duplicates2 = set()
    new_list = []
    index = 0
    while index < len(list_no_duplicates):
        item = list_no_duplicates[index]
        if item not in duplicates2:
            new_list.append(item)
            duplicates2.add(item)
        index +=1
    return new_list

names = ["Chris", "Kevin", "Naveed", "Pete", "Victor", "Chris", "Kevin"]
print(f'18. The list of names without duplicates is: {no_duplicates(names)}')

# Ex 19: Write a function that gets an list of strings as parameter and returns a new list containing all the values from the
# provided list in the same order but without any duplicated values. If the string ‘pete’ is a value inside the list your
# function should skip it and not copy it to the new list. In your solution use only while loops.
# For example: names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', ‘Chris’, ‘Kevin’]
# Function output should be: ['Chris', 'Kevin', 'Naveed', 'Victor']

def no_pete(list_no_duplicates):
    duplicates2 = set()
    new_list = []
    index = 0
    while index < len(list_no_duplicates):
        item = list_no_duplicates[index]
        if item == "Pete":
            index += 1
            continue
        if item not in duplicates2:
            new_list.append(item)
            duplicates2.add(item)
        index +=1
    return new_list

print(f'19. The list of names without duplicates and the name Pete is: {no_pete(names)}')

# Ex 20: Use a while loop to iterate on a boolean list. As long as the next index is different from the previous index the
# iteration continues, otherwise, return the index of the element with the same value. If there are not two successive values,
# the function will return -1.
# For example:
# list1= [true, false, false, true, true, false] → return 2
# list2= [true, false, true, false, true, true]; → returns 5
# list3= [true, false, true, false, true, false]; → returns -1

def check_booleans(list_booleans):

    val = 1
    while val < len(list_booleans):
        if list_booleans[val] == list_booleans [val -1]: #It checks if the indexes are the same, starting with index 1
            return val
        val += 1
    return  -1

list1= [True, False, False, True, True, False]
print(f'20.1. First boolean check: {check_booleans(list1)}')

list2= [True, False, True, False, True, True]
print(f'20.2. First boolean check: {check_booleans(list2)}')

list3= [True, False, True, False, True, False]
print(f'20.3. First boolean check: {check_booleans(list3)}') #If none matches are found, will return -1.

# Ex 21: Write a python program that gets user input (use input() function for this). The first input will be the user full name.
# Second input will be the user age. Third input will be the user email
# Write validation for each input provided by the user and allow the user to try again in case the user provided invalid input.
# Validation for full name input → string type with 2 words for first name and last name.
# Validation for age input → int type between 1 - 130.
# Validation for email input → string type with ‘@’ inside.


def get_user_details():
    while True:
        full_name = input("21. Enter your full name (First and Last name): ")
        name_parts = full_name.split()
        if len(name_parts) == 2 and all(part.isalpha() for part in name_parts):
            break
        else:
            print("Invalid input. Please enter your first and last name (only alphabetic characters).")
    while True:
        try:
            age = int(input("21. Enter your age (between 1 and 130): "))
            if 1 <= age <= 130:
                break
            else:
                print("Age must be between 1 and 130. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")
    while True:
        email = input("21. Enter your email address: ")
        if '@' in email:
            break
        else:
            print("Invalid email format. Please include '@' in the email.")
    print(f' 21. User Details: - Full Name: {full_name}, - Age: {age}, - Email: {email}')

get_user_details()
