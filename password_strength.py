import re
def calculate_strength(password):
    """
    Calculates the strength of a password based on several criteria
    :param password: the password to check
    :return: password strength as an integer (1-10)
    """
    strength = 0
    feedback = []

    if len(password) > 8:
        strength += 2
    else:
        feedback.append("Your password could be longer.")
    
    if re.search(r'[A-Z]', password):
        strength += 2
    else:
        feedback.append("Your password could use more uppercase letters.")

    if re.search(r'[a-z]', password):
        strength += 2
    else:
        feedback.append("Your password could use more lowercase letters.")

    if re.search(r'[0-9]', password):
        strength += 2
    else:
        feedback.append("Your password could use more numbers.")

    if re.search(r'[_@#$%^&*()<>?/\|}{~:]', password):
        strength += 2
    else:
        feedback.append("Your password could use more special characters.")
    
    return strength, feedback



password = input("Enter a password: ")
strength, feedback = calculate_strength(password)
print("Password strength: ", strength)
if feedback:
    print("Here are some ways you could improve your password:")
    for suggestion in feedback:
        print("- ", suggestion)

def repeat_password_check():
    while True:  # This creates an infinite loop
        password = input("\nEnter a password (or type 'exit' to quit): ")
        
        # If the user types 'exit', break out of the loop
        if password.lower() == 'exit':
            break

        strength, feedback = calculate_strength(password)
        print("\nPassword strength: ", strength)
        if feedback:
            print("Here are some ways you could improve your password:")
            for suggestion in feedback:
                print("- ", suggestion)

repeat_password_check()



input('Press ENTER to exit')
