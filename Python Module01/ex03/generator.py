import random

def generator(text, sep, option=None):
    if not isinstance(text, str):
        yield "Error"
        return

    words = text.split(sep)
    if option == "shuffle":
        random.shuffle(words)
    elif option == "unique":
        words = list(set(words)) # Set removes duplicates and list converts it back to a list.
    elif option == "ordered":
        words = sorted(words)
    else :
        yield "Error"
        return
    
    for word in words:
        yield word
        

