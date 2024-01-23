

def greet():
    print("hey")


greet()


# Example 2: throws error, functions are not hoisted as in JS
# NameError: name 'greet2' is not defined. Did you mean: 'greet'?

greet_again()


def greet_again():
    print("hello again")
