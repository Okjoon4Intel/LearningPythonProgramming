from string import Template


def main():
    # Python overloads the % operator to work on string
    str0 = 'That is %d %s bird!' % (1, 'dead')
    print(str0)

    str0 = "%s --- %s -- %s" % (42, 3.14159, [1, 2, 3])
    print(str0)

    # Usual string formatting with format()
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # create a template with placeholders
    templ = Template("You're watching ${title} by ${author}")
    
    # use the substitute method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)
    
    # use the substitute method with a dictionary
    data = { 
        "author": "Joe Marini",
        "title": "Advanced Python"
    }
    str3 = templ.substitute(data)    
    print(str3)

    
if __name__ == "__main__":
    main()
    