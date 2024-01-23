# global and local scope


name = 'david'
color = "red"


def get_name():
    global name     # "global" keyword, sets to global scope
    name = 'teddy'  # overrides global, otherwise would be local scope
    color = "blue"
    print(color)    # blue


get_name()


print(name)  # teddy
print(color)  # global, red
