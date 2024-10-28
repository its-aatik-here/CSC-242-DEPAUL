def findTarget(nested_list, target):
    for item in nested_list:
        if isinstance(item, list):
            if findTarget(item, target):
                return True
        elif item == target:
            return True
    return False

def countVowels(s):
    if not s:
        return 0
    vowels = 'aeiouAEIOU'
    return (1 if s[0] in vowels else 0) + countVowels(s[1:])

def sumDigits(n):
    if n == 0:
        return 0
    return n % 10 + sumDigits(n // 10)

def countOccur(character, my_string):
    if not my_string:
        return 0
    return (1 if my_string[0].lower() == character.lower() else 0) + countOccur(character, my_string[1:])

def nested_sum(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total
