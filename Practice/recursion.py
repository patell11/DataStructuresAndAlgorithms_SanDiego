
## function to calculate the sum of the list using recursion

def listSum(numlst):
    if len(numlst) == 1:
        return numlst[0]
    else:
        return numlst[0] + listSum(numlst[1:])

print(listSum([1,2,3,4,5]))


## function to change the given number to any base using recursion

def toStr(n, base):
    convertstring = "0123456789ABCDEF"
    if n < base:
        return convertstring[n]
    else:
        return toStr(n//base, base) + convertstring[n%base]

print(toStr(1453,16))

## function to change the given number to any base using the stack
from stack import Stack
def toStrStack(n,base):
    convertstring = "0123456789ABCDEF"
    basestack = Stack()

    while n > 0:
        if n < base:
            basestack.push(convertstring[n])
        else:
            basestack.push(convertstring[n%base])
        n = n//base

    result = ""
    while not basestack.isEmpty():
        result = result + str(basestack.pop())
    return result

print(toStr(1453,16))

## Tower of Hanoi
def moveTower(height, frompole, topole, withpole):
    if height >= 1:
        moveTower(height-1, frompole, withpole, topole)
        moveDisk(frompole, topole)
        moveTower(height-1, withpole, topole, frompole)

def moveDisk(ffrom, to):
    print("Moving Disk from " + ffrom + " to " + to )

moveTower(3,"A","C","B")

def dpMakeChange(coinValueList,change,minCoins):
    for cents in range(change+1):
        print("for cents in ", cents)
        coinCount = cents
        print("coinCount = ", coinCount)
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            print("    J in ", j)
            print("    minCoins coinCount", minCoins[cents-j] + 1, coinCount)
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j

        minCoins[cents] = coinCount
        print(minCoins)
    return minCoins[change]

coinCount = [0]*(10+1)
print(dpMakeChange([1,5,6,9], 10, coinCount))
