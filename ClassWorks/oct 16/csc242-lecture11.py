##do work on the way down
def printLst(lst):
    if len(lst)==0:
        return 
    else:
        print(lst[0])
        printList(lst[1:])
##do work on the way up
def printLst(lst):
    if len(lst)==0:
        return
    else:
        printLst(lst[:-1])
        print(lst[-1])

def cheer(n):
    if n<=1:
        print('Hurrah')
    else:
        print('Hip')
        cheer(n-1)

def makeCheer(n):
    if n<=1:
        return 'Hurrah!'
    else:
        s = makeCheer(n-1)
        return 'Hip '+s


def pattern(n):
    if n ==1:
        print("1",end = ' ')
    else:
        pattern(n-1)
        print(n, end=' ')
        pattern(n-1)


def makePattern(n):
    if n ==1:
        return '1'
    s = makePattern(n-1)
    #return s +' '+str(n)=" "+s
    return f'{s} {n} {s}'



def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)
    

