# Functions allow you to reuse and organize parts of your code
# Create a function using def <function_name>():

# Function definitions simply tell the interpreter that the function exists
# No code is executed until the function is "called"
def function_1():
    print("I am function 1")


def function_2():
    print("I am function 2")

# This is how you call the functions
function_1()
function_2()

# Functions can take parameters
# In this case, "number" is a local variable within this function
# The value of "number" must be "passed in" to the function when it is called
def print_number(number):
    print(number)

# Here is how you call a function with parameters
print_number(10)
print_number(15)

# Functions can take multiple parameters
def print_sum(number1, number2):
    print(number1 + number2)

print_sum(10, 20)

# Functions can also return values to the caller
def return_ten():
    return 10

# Number is a variable which will be initialized with
# the return value of the function
number = return_ten()

print(return_ten())

# All of these things can be combined at the same time

def square_number(number):
    return number * number

print("The square of 8 is {}".format(square_number(8)))

# Side note about the above string formatting
# The "{}" indicates a placeholder for where text will go
# The value inside the .format(<value>) will be placed into the "{}"
# For example, this statement
message = "The number is {}".format(10)

# Will store the value "The number is 10" inside the variable
print(message)