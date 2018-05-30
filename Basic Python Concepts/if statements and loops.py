# If statements are used to make decisions based on a conditional statement
# for example, the value in a variable could be used

variable1 = True
variable2 = False

if variable1:
    print("True")

# else if statements can be added to check for additional conditions

if variable1:
    print("Variable 1 is True")
elif variable2:
    print("Variable 2 is True")

# else statements can be added as a sort of "default" for when none of the other
# conditions are met

if variable1:
    print("Variable 1 is True")
elif variable2:
    print("Variable 2 is True")
else:
    print("Variable 1 and Variable 2 are both False")

# Remember that only one of the available branches in an if statement is executed

# Also remember OR and AND operators

if variable1 or variable2:
    print("Variable 1 or Variable 2 is True (or possibly both)")

if variable1 and variable2:
    print("Variable 1 and Variable 2 are both True")

# Now fixed count loops
# Count to 10 and print 0 - 9
# i is the index for each loop
for i in range(10):
    print(i)

# Python allows easy looping through lists as well

list1 = ["Hello", "There", "Alex"]

for i in list1:
    print(i)

# While loops repeat steps until a condition is false
# Count to 10 and print 0 - 9
count = 0

while count != 10:
    print(count)
    count += 1

# This is commonly used as an infinite loop
while True:
    # "break" leaves a loop early
    break
    
# "continue" skips the rest of the code in a loop and moves to the next iteration
# Print 0 - 9 but skip 5
for i in range(10):
    if i == 5:
        continue

    print(i)
