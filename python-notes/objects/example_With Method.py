
# in JS
"""
let person = {
    name: "buddy",
    age: 30,
    getCoffee: () => {
        console.log("got coffee");
    }
};

person.getCoffee();
"""

# in Python:

person = {
    'name': 'buddy',
    'age': 30,
    'get_coffee': lambda: print('got coffee')
}

# Call the get_coffee method
person['get_coffee']()


# in Python, class approach
class Person:
    def __init__(self, name, age):
        self.name = name  # "self" is the python version of "this" in JS
        self.age = age

    def get_coffee(self):
        print("got coffee")


# Create an instance of the Person class
person = Person(name="buddy", age=30)

# Call the get_coffee method
person.get_coffee()


# if your function was more involved break out
def get_coffee():
    # More involved logic for getting coffee
    print('Preparing coffee...')
    print('Pouring coffee...')
    print('Got coffee!')


person = {
    'name': 'buddy',
    'age': 30,
    'get_coffee': get_coffee
}

# Call the get_coffee method
person['get_coffee']()


# this apporach is very uncommon in Python
person = {
    'name': 'buddy',
    'age': 30,
    'get_coffee': (lambda:
                   print('Preparing coffee...'),
                   print('Pouring coffee...'),
                   print('Got coffee!'))[0]
}

# Call the get_coffee method
person['get_coffee']()
