import code


def printLst(lst):
    'print a list lst, one element per line, non-destructively'
    if len(lst) > 0:
        print(lst[0])
        printLst(lst[1:])
            
def listPrint(lst):
    'print elements of a multi-dimensional list, one per line'
    for elem in lst:
        if type(elem) == list:
            listPrint(elem)
        else:
            print(elem)


def listPrint(n):
    'print elements of a multi-dimensional list, one per line'
    if len(n)<1:
        return n
    elif type (n[0]) == list:
        listPrint (n[0])
        listPrint (n[1:])
    else:
        print(n[0])
        listPrint(n[1:])


def countint(lst):
    if len(lst)  == 0:
        return 0
    elif type(lst[0]) == int:
        return 1 + countint(lst[1:])
    elif  type(lst[0]) == list:
        return countint(lst[0]) + countint(lst[1:])
    else:
        return countint(lst[1:])

def findmax(lst):
    if len(lst) == 0:
        return 0
    elif type(lst[0]) == int or type (lst[0]) == float:
        val = findmax(lst[1:])
        if lst[0] > val:
            return lst[0]
        else:
            return val
    elif type (lst[0]) == list:
        val1 =  findmax(lst[0])
        val2 = findmax(lst[1:])
        if val1  > val2:
            return val1
        else:
            return val2
    else:
        return  findmax(lst[1:])










code.interact(local=dict(globals(), **locals()))