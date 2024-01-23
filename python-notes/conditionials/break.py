

fruits = ['apple', 'orange', 'pear', 'persimmon']

for i in fruits:
    if i == 'pear':
        print(f'{i}, that is the fruit for me.')
        # once the condition is met we break out of the loop, no need to continue in this case.
        break
    elif i == 'apple':
        print(f'i would consider a: {i}')
    else:
        print(f"I don't want a: {i}")

#output:
# i would consider a: apple
# I don't want a: orange
# pear, that is the fruit for me.