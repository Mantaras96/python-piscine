import sys

a = 0
b = 0
result = 0

if (len(sys.argv) == 3 and sys.argv[1].isnumeric() and sys.argv[2].isnumeric()):
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print (f"Sum: {a + b}")
    print (f"Difference: {a - b}")
    print (f"Product: {a * b}")
    if (b != 0):
        print (f"Quotient: {a / b}")
        print (f"Remainder: {a % b}")
    else:
        print ("Error division by zero")
        print ("Error module by zero")
else :
    print('Error with parameters')

