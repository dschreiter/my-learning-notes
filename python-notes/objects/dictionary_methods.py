
"""
In Python 3, dictionaries come with a variety of useful methods for manipulating and retrieving data.
Here are some of the most common dictionary methods:
"""

# keys(): Returns a view of all keys in the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()

# values(): Returns a view of all values in the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()

# items(): Returns a view of all key-value pairs (tuples) in the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()

# get(key, default=None): Returns the value for the given key. If the key is not found, it returns the default value (default is None if not specified).
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')

# pop(key, default=None): Removes and returns the value for a given key. If the key is not found, it returns the default value (or raises a KeyError if default is not provided).
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')

# popitem(): Removes and returns the last key-value pair as a tuple.
my_dict = {'a': 1, 'b': 2, 'c': 3}
key, value = my_dict.popitem()

# update(iterable): Updates the dictionary with elements from another iterable or from keyword arguments.
my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 3, 'c': 4})

# clear(): Removes all items from the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
