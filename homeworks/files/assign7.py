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
        if link.strip():  # Check if link is not empty
            crawl(link)