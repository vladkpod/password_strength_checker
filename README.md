# password_strength_checker
 A python script to check the strength of your password and suggest changes

```markdown
# Python Password Strength Calculator

This project creates a simple password strength calculator using Python's built-in `re` module for regular expressions.

## How It Works

First, the script imports the required libraries:

```python
import re
```

Then, we create a function to calculate password strength. This function checks the password against different criteria and returns a strength rating:

```python
def calculate_strength(password):
    """
    Calculates the strength of a password based on several criteria
    :param password: the password to check
    :return: password strength as an integer (1-10)
    """
    strength = 0
    if len(password) > 8:
        strength += 2
    if re.search(r'[A-Z]', password):
        strength += 2
    if re.search(r'[a-z]', password):
        strength += 2
    if re.search(r'[0-9]', password):
        strength += 2
    if re.search(r'[_@#$%^&*()<>?/\|}{~:]', password):
        strength += 2
    return strength
```

The function works by checking the following criteria:

- The password is longer than 8 characters.
- The password contains uppercase letters.
- The password contains lowercase letters.
- The password contains numbers.
- The password contains special characters.

Each criterion met increases the strength rating by 2 points, resulting in a rating between 0 and 10.

## Testing The Function

To test this function, call it with different passwords:

```python
print(calculate_strength("simplepassword"))   # Should return 4
print(calculate_strength("ComplexPassword123"))  # Should return 8
print(calculate_strength("VeryComplexPassword123!"))  # Should return 10
```

## User Input

To allow users to check the strength of their own passwords, we use the `input()` function:

```python
password = input("Enter a password: ")
strength, feedback = calculate_strength(password)
print("Password strength: ", strength)
if feedback:
    print("Here are some ways you could improve your password:")
    for suggestion in feedback:
        print("- ", suggestion)
```

This will prompt the user to enter a password, then print out its strength rating.

## Repeat Password Check

Finally, we add a function to allow repeated password checks:

```python
def repeat_password_check():
    while True:
        password = input("\nEnter a password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break
        strength = calculate_strength(password)
        print("\nPassword strength: ", strength)
repeat_password_check()
```

This function will keep asking for a password and printing its strength until the user types 'exit'.
```

This provides a good starting point for a password strength calculator. Further enhancements could include penalizing repeated characters, common words, or sequences of numbers or letters, or rewarding less common special characters or longer passwords.
