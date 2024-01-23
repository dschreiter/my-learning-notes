# key word arguments


# and **kwargs would be specific to dicitonaries i.e the "key" as in KW

# Yes, that's correct. In a function definition, **kwargs allows you to pass a variable number of keyword arguments, and these arguments will be collected into a dictionary. The keys of the dictionary correspond to the parameter names, and the values are the values you pass during the function call.

# Here's an example:

def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Using a dictionary as **kwargs
example_function(first_name="John", last_name="Doe", age=25)

# Using individual key-value pairs as **kwargs
example_function(city="New York", country="USA")
