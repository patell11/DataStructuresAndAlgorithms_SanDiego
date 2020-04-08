# Checking the anagram by each character from string 1 to the characters in string 2
def anagramSolution1(s1, s2):
    stillOk = True
    if len(s1) != len(s2):
        stillOk = False

    alist = list(s2)
    pos1 = 0
    while pos1 < len(s1) and stillOk:
        print("Checking" + str(pos1))
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            print("Iteration " + str(pos2) + " for " + str(pos1))
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None
        else:
            stillOk = False
        pos1 += 1
    return stillOk


print(anagramSolution1('amit','taim'))

## Checking the anagram by sorting the strings first and then comparing them by their position
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True
    while pos < len(alist1) and matches:
        if alist1[pos] ==  alist2[pos]:
            pos += 1
        else:
            matches = False

    return matches

print(anagramSolution2('amit','taim'))

## Checking the anagram by counting the number of occurences of the characters in each strings and comparing them.

def anagramSolution3(s1,s2):
    c1 = [0]* 26
    c2 = [0]* 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    matches = True
    while j < 26 and matches:
        if c1[j] == c2[j]:
            j += 1
        else:
            matches = False
    return matches

print(anagramSolution3('amit','taim'))