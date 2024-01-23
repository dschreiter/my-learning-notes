"""

In Python, the pass statement is a no-operation statement. 
It serves as a placeholder where syntactically some code is required, 
but you don't want to perform any actions. 
It's often used in situations where the Python syntax requires a statement, 
but you don't want to execute any specific code.

If you have a loop or a conditional statement and you use pass, 
it essentially means "do nothing." It won't affect the loop or the program's flow, 
and it will continue to the next iteration or statement.
"""

for i in range(5):
    if i == 2:
        pass  # do nothing for i == 2, this is a syntax requirement
    else:
        print(i)

#Outputs:
# 0
# 1
# 3
# 4