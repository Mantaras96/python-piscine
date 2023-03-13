import sys
import string


def text_analyzer(*args):
    upper = 0
    lower = 0
    punctuations = 0
    space = 0
    if (len(args) > 1):
        print('AsserionError: more than one argument are provided or no provided')
        return
    elif (len(args) == 0):
        print("What is the text to analyse?")
        sys.stdout.flush()
        str = sys.stdin.readline()
        space -= 1
    elif (args[0].isnumeric()):
        print('AssertionError: argmuent is not a string')
        return

    else:
        str = args[0]
    for letter in str:
        if letter in string.ascii_lowercase:
            lower += 1
        elif letter in string.ascii_uppercase:
            upper += 1
        elif letter in (string.punctuation):
            punctuations += 1
        elif letter in (string.whitespace):
            space += 1
    print("The text contains {} characters:".format(len(str)))
    print("- {} upper letters".format(upper))
    print("- {} lower letters".format(lower))
    print("- {} punctuation marks".format(punctuations))
    print("- {} spaces".format(space))

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        text_analyzer()
    else:
        text_analyzer(*sys.argv[1:])
            
            