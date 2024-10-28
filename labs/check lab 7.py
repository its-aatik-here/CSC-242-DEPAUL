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
