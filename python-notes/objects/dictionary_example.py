# Creating a dictionary (equivalent to an object in JavaScript)
person = {
    'name': 'John',
    'age': 25,
    'isStudent': True,
    'address': {
        'city': 'Example City',
        'country': 'Example Country'
    }
}

def say_hello():
    print(f"Hello, my name is {person['name']}!")


# Calling the function
say_hello()  # Output: Hello, my name is John!

"""
In this Python code:

We use curly braces {} to define a dictionary.
The keys in the dictionary are strings, and the values can be of any data type, including nested dictionaries.
We access dictionary values using square brackets ([]).
We define a function (say_hello) within the dictionary to mimic a method.
We call the function to produce a similar output.
While Python doesn't have a direct equivalent to JavaScript's object literal syntax, 
dictionaries serve a similar purpose and are commonly used for representing structured data.
"""
