# int a variable, but assign no value
# None, is the same as null in JS
x = None


# Python doesn't have a way to declare constants, uppercase is the convention but this is not enformced
MY_CONSTANT = 42
MY_CONSTANT = 555  # this just overwrote the variable without issue.

# the init variable x now assigned
x = 12

print(x, MY_CONSTANT)
