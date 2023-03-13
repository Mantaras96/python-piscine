import sys

if (len(sys.argv) > 2 or len(sys.argv) == 1):
    print('AsserionError: more than one argument are provided or no provided')
elif (sys.argv[1].isnumeric()):
    if (int(sys.argv[1]) == 0):
        print("Number is zero")
    elif (int(sys.argv[1]) % 2 == 1):
        print ("I'm odd.")
    else:
        print("I'm Even.")
else:
    print('AssertionError: argument is not intenger.')