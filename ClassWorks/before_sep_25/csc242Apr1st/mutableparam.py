def secondFcn(lst):
    'this is a doc string for the second function which changes a list'
    print("In secondFcn, before the assignment")
    print(lst)
    lst[0] = 5
    print("In secondFcn, after the assignment")
    print(lst)

def firstFcn():
    'this is a doc string for the first function which calls the second function'
    lst = [3, 6, 9, 12]
    print(lst)
    print("In firstFcn, before the call to secondFcn")
    secondFcn(lst)
    print("In firstFcn, after the call to secondFcn")
    print(lst)

