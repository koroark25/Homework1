#problem 1
print(type("Rosewater"))
print(type(0.001))
print(type(37))
print(type(False))

#problem 2
#The + (plus) operator combines two strings together how they are
#Meanwhile, the , (comma) operator combines two strings together with a space between them.
#Examples:
print("Comma Example: Hey","I'm here.")
print("Plus Example: Hey"+ "I'm here.")

#problem 3
#str function
print(str(87))
#int function
print(int(5.4))
#float function
print(float(45))

#by using \n you can force the string to move to another line, allowing you to print multiple lines in one print statement
#example
print("The drooping willow, bowing low,\nAffords no aid to him who lies beneath; \nIts leaves are dry,",
      "its water far away. \nYet, though forsaken by man, it stands,\nWith constant memory of past times.")

#problem 5
flour = 2
milk = 1
egg = 4
oil = .4
vanilla = .012
cake = 2 * flour + 0.5 * (milk - egg + vanilla) + oil**2
print(cake)
