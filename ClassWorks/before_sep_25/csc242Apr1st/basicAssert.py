#from assertImport import *

# Some functions to demonstrate basic assertions

def sumPos(lst):
    'return the sum of the positive numbers in the list lst'
    total = 0
    for num in lst:
        if num > 0:
            total += num
    return total

def sumLen(lst):
    'return the sum of the lengths of the strings in the list lst'
    total = 0
    for astr in lst:
        total += len(astr)
    return total

##def countAdverb(phrase):
##    'return the number of adverbs in phrase'
##    phrase = removePunc(phrase.lower())
##    total = 0
##    for word in phrase.split():
##        if word.endswith('ly'):
##            total += 1
##    return total

