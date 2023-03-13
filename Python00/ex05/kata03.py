import sys

kata = "The right format"
result = ""
i = 0

print (42 - len(kata))

while i < 42 - len(kata):
    result += "-"
    i += 1

print (result + kata)