# Python overloads the % operator to work on string
str0 = 'That is %d %s bird!' % (1, 'dead')
print(str0)

str0 = "%s --- %s -- %s" % (42, 3.14159, [1, 2, 3])
print(str0)

# Usual string formatting with format()
str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
print(str1)
