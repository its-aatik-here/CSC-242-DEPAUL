


def find_depth(lst, depth=1):
    if not (type(lst) is list):
        return 0  
    if len(lst) == 0:
        return depth
    max_depth = depth
    for item in lst:
        if type(item) is list:
            current_depth = find_depth(item, depth + 1)
            max_depth = max(max_depth, current_depth)

    return max_depth

import os

def vigilante_search(filename, directory):
    try:
        if filename in os.listdir(directory):
            print(os.path.join(directory, filename))
            return
    except FileNotFoundError:
        print("Directory not found")
        return
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            vigilante_search(filename, item_path)

    print("None Found")

import os

def traverse(pathname, depth=0):
    try:
        contents = os.listdir(pathname)
    except FileNotFoundError:
        print(f"Directory '{pathname}' not found.")
        return
    print('  ' * depth + (pathname.split('/')[-1] + '/' if os.path.isdir(pathname) else pathname))

    for item in contents:
        item_path = os.path.join(pathname, item)
        if os.path.isdir(item_path):
            traverse(item_path, depth + 1)
        else:
            print('  ' * (depth + 1) + item)
