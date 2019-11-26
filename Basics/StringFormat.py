# Import libraries


# Main Function
def main():
    age = 20
    name = "Swaroop"
    book = "A Byte Of Python"

    # Method I: {0} is the first argument and {1} is the second argument
    print('{0} was {1} years old when he wrote this book'.format(name, age))
    print('Why is {0} playing with that python?'.format(name))

    # Method II: Numbers are optional
    print('{} was {} years old when he wrote this book'.format(name, age))
    print('Why is {} playing with that python?'.format(name))

    # Method III: Name the parameters
    print('{name} was {age} years old when he wrote this book'.format(age=age, name=name))
    print('Why is {name} playing with that python?'.format(name=name))

   # Method IV: f-strings
    print(f'{name} was {age} years old when he wrote this book')
    print(f'Why is {name} playing with that python?')

    # decimal (.) precision of 3 for float '0.333'
    print('{0:.3f}'.format(1.0/3))

    # Fill with underscores(_) with the text centered
    # (^) to 11 width '___hello___'
    print('{0:_^11}'.format('hello'))

    # Keyward-based 'Swaroop wrote A Byte of Python'
    print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

    # Print with a blank. By default, the print function will all print on a separate line each.
    print('a', end=' ')
    print('b', end=' ')
    print('c')


if __name__ == "__main__":
    main()