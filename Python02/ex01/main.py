
class ObjectC(object):
    def __init__(self):
        pass

def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()
    i = 0
    for arg in args:
        setattr(obj, 'var_' + str(i), arg)
        i += 1
    for key, value in kwargs.items():
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)
    return obj

def doom_printer(obj):
    if obj is None:
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end of doom_printer")

def main():
    obj = what_are_the_vars(8) # Esto son args normales
    doom_printer(obj)
    obj = what_are_the_vars(8, 9, 10)
    doom_printer(obj)
    obj = what_are_the_vars(hello="world") # Esto son kwargs (clave="valor")
    doom_printer(obj)

if __name__ == "__main__":
    main()