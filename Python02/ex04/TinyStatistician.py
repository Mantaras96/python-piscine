from TinyStatistician import TinyStatistician


def mean(x):
    if len(x) == 0:
        return None
    return sum(x) / len(x)

def median(x):
    if len(x) == 0:
        return None
    x = sorted(x)
    mid = len(x) // 2
    if len(x) % 2 == 0:
        return (x[mid] + x[mid - 1]) / 2
    return x[mid]

def quartiles(x):
    if len(x) == 0:
        return None
    else:
        x = sorted(x);
        mid = len(x) // 2
        if len(x) % 2 == 0:
            lower = x[:mid]
            upper = x[mid:]
        else:
            lower = x[:mid]
            upper = x[mid + 1:]
        return median(lower), median(upper)

def variance(self, x):
    if len(x) == 0:
        return None
    x = sorted(x)
    x_mean = self.mean(x)
    return sum([(x_i - x_mean) ** 2 for x_i in x]) / len(x)


def standardDeviation(x):
    if len(x) == 0:
        return None
    return sum((x_i - mean(x)) ** 2 for x_i in x) / len(x)


def	main( ):
    print("Hello World")
    
if __name__ == "__main__":
    main()   