# Demonstrate the use of keyword-only arguments

# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, suppressException=False):
    print(arg1, arg2, suppressException)


def main():
    # try to call the function without the keyword
    #myFunction(1, 2, True) # ERROR
    myFunction(1, 2, suppressException=True)


if __name__ == "__main__":
    main()
