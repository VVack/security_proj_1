#!/usr/bin/python3

import sys
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)


def mean_var(size, s):
    tempStrings = []
    retVal = 0
    for counter in range(0, size):
        #print(counter, size)
        tempStrings.append(s[counter::size])
        retVal += pop_var(tempStrings[counter])
    return retVal/size
def chi_square (s):
    count = Counter(s)
    sum = 0
    for c in alphabet:
        sum += (((count[c]/len(s) - letter_freqs[c])**2)/letter_freqs[c])
    return sum




def crack_caesar(start, size, s):
    subString = s[start::size]
    chiScores = []
    for counter in range(0,25):
        tempStr = ''
        for x in subString:
            pos = alphabet.find(x)
            newPos = (pos-counter) % 26
            newChar = alphabet[newPos]
            tempStr += newChar
        chiScores.append(chi_square(tempStr))
    #print('chi squared scores', chiScores)
    return alphabet[chiScores.index(min(chiScores)): chiScores.index(min(chiScores))+1]




if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()





    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
    meanVars = []
    maxVal = 0
    maxIndex = 0
    keyLength = 2
    key = ''
    for x in range(0, 11):
        meanVars.append(mean_var(int(x+2), cipher))
        if meanVars[x] > maxVal:
            maxVal = meanVars[x]
            maxIndex = x
    #print(meanVars)
    #print(maxIndex)
    keyLength+= maxIndex
    for i in range(0, keyLength):
        key += crack_caesar(i, keyLength, cipher)
    print(key)


