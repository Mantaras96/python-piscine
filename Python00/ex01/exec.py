import sys

i = 1
arr = ''

while i < len(sys.argv):
    arr += sys.argv[i]
    if ( i != len(sys.argv) - 1):
        arr += ' '
    # print(sys.argv[1])
    i += 1

print(arr)
arr = arr[::-1]
print(arr)