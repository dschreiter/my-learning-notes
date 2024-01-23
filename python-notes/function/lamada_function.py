"""
In Python, a lambda function is a concise way to create anonymous functions.
"Anonymous" means that a lambda function doesn't have a name.
You can use lambda functions when you need a simple function for a short 
period and don't want to formally define it using the def keyword.
"""

#Example

add = lambda x, y: x + y
print(add(2, 3))  # Outputs 5


"""
in JS:

const add = (x,y)=> {
    x+y
}

"""

"""
In this example, lambda x, y: x + y creates an anonymous function
that takes two arguments x and y and returns their sum. 
The lambda keyword is followed by the arguments, a colon, and the expression.

Lambda functions are often used for short-lived operations
or as arguments to higher-order functions that accept functions
as parameters (e.g., map, filter, sorted). 
However, for more complex functions, 
it's generally recommended to use the def keyword and define a regular function.
"""