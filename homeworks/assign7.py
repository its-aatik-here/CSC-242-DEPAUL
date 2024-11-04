# Exercise 1

def string_cleaning(s):
    if len(s)<=1:
        return s
    if s[0]==s[1]:
        return string_cleaning(s[1:])
    else:
        return s[0] + string_cleaning(s[1:])


# Exercise 2

import os
def crawl(filename):
    print(f"Visiting {filename}")
    file = open(filename, 'r')
    links = file.read().splitlines()
    file.close()
    for link in links:
        if link.strip():
            crawl(link)


#  Exercise 3

def pascal(n):
    if n == 0:
        return [1]
    previous_row = pascal(n-1)
    current_row = [1]
    for i in range(1, len(previous_row)):
        current_row.append(previous_row[i-1] + previous_row[i])
    current_row.append(1)
    return current_row


# Exercise 4

def nestPair(s):
    if len(s) == 0:
        return False
    if s[0] == (')'):
        return False
    if s.count("(") != s.count(")"):
        return False
    par = 0
    for char in s:
        if char == "(":
            par += 1
        elif char == ")":
            par -= 1
    if par < 0:
        return False
    return par == 0

# Exercise 5


import os
def findLongNames(directory):
    long_names = [] 
    files = os.listdir(directory)
    for filename in files:
        name_parts = filename.rsplit(".")
        name = name_parts[0]
        if len(name)>10:
            long_names.append(filename)
    return long_names

