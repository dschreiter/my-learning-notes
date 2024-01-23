def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division successful!")
    finally:
        print("This block always executes, whether there is an exception or not.")


# Example usage
try:
    divide_numbers(10, 2)
    divide_numbers(10, 0)  # This will raise a ZeroDivisionError
    divide_numbers("abc", 2)  # This will raise a TypeError
except Exception as e:
    print(f"Exception caught outside the function: {e}")


