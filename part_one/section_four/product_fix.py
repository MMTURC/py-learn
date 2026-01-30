"""

This program asks the user for three numbers. The program then prints out their product, that is, 
the numbers multiplied by each other. There is, however, something wrong with the program - it doesn't
work quite right, as you can see if you run it.

An example of the expected execution of the program:

Sample output

Please type in the first number: 2
Please type in the second number: 3
Please type in the third number: 5
The product is 30


"""


number_one = int(input("Please type in the first number: "))
number_two = int(input("Please type in the second number: "))
number_three = int(input("Please type in the third number: "))

product = number_one * number_two * number_three

print("The product is", product)

