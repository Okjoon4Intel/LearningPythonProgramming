# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# Implement the Fibonacci algorithm
def fibonacci(n):
    "Return a Fibonacci series up to n"
    ret = []
    a, b = 0, 1
    while b < n:
        ret.append(b)
        a, b = b, a + b
    return ret

# Call functions here
func1()
print(func1()) # Print the return value from the function
func2(10, 20)
print(func2(10, 20))
print(cube(3))
print(power(2))
print(power(2, 3))
print(power(x=3, num=2))
print(multi_add(4, 5, 10, 4))

print(fibonacci(10))
print(fibonacci(100))
print(fibonacci(1000))