import os

def countFiles(pathname):
    count = 0
    for item in os.listdir(pathname):        
        n = os.path.join(pathname, item)
        if os.path.isdir(n):
            count += countFiles(n)
        else: 
            count += 1
    return count

def search(fname, path):
    for item in os.listdir(path):
        itemPath = os.path.join(path, item)
        if os.path.isfile(itemPath):
            if item.lower() == fname.lower():
                return itemPath
        elif os.path.isdir(itemPath):
            p = search(fname, itemPath)
            if p != None:
                return p
    return None
