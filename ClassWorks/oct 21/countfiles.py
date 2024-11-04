import os

def countFiles(filename):
    count = 0
    for item in os.listdir(pathname):
        n = os.path.join(pathname,item)
        if os.path.isdir(n):
            rec =  countFiles(n)
        else:
            count += 1
    return count
