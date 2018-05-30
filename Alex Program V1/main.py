# Return the correct response for a given message
def process_message(message):
    if message == "hi" or message == "hello":
        return "Hello!"
    elif message == "you suck":
        return "ur mum gay"
    elif message == "bye":
        return "Goodbye!"
    elif message == "echo":
        return "echo"
    elif message == "marco":
        return "polo"
    else:
        return "I don't understand that"

# Tell the user that they are using this fabulous program
print("Welcome to Alex Program V1\n")

# Loop until we break from inside
while True:
    # Read input from the user
    message = input("Please type a message:\n")

    # Make the entire message lower-case
    message = message.lower()

    # Exit if the message is "exit"
    if message == "exit":
        break

    # Respond to the message
    print(process_message(message) + "\n")

# Thank the user for their time
print("Thank you for using Alex Program V1! We hope to see you again!")
