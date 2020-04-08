from stack import Stack

def baseConverter(decNumber, base):

    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber//base
    convertedString = ""
    while not remstack.isEmpty():
        convertedString = convertedString + digits[remstack.pop()]

    return convertedString

print(baseConverter(25,2))
print(baseConverter(25,16))

