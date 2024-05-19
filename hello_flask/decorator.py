# Functions inputs/functionality/output
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2


# First-class objects, can be passed around as arguments e.g. int/string etc.
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)


# result = calculate(add, 1, 3)
# print(result)


# Nested functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
#
# outer_function()


# Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function()


import time


# Python Decorator Function
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


say_hello()
decorated_function = delay_decorator(say_greeting)
decorated_function()
