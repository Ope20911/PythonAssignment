# 1. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# 2. IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"IndexError: {e}")

# 3. ValueError
try:
    number = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# 4. KeyError
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
except KeyError as e:
    print(f"KeyError: {e}")

# 5. TypeError
try:
    result = "string" + 6
except TypeError as e:
    print(f"TypeError: {e}")

# 6. FileNotFoundError
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# 7. AttributeError
try:
    obj = "string"
    obj.some_method()
except AttributeError as e:
    print(f"AttributeError: {e}")

# 8. ImportError
try:
    import nonexistent_module
except ImportError as e:
    print(f"ImportError: {e}")

# 9. NameError
try:
    print(undeclared_variable)
except NameError as e:
    print(f"NameError: {e}")

# 10. NotImplementedError
class MyClass:
    def my_method(self):
        raise NotImplementedError("This method needs to be implemented")

try:
    obj = MyClass()
    obj.my_method()
except NotImplementedError as e:
    print(f"NotImplementedError: {e}")
