# import code 

#EXERCISE 1

def remove_whitespace (word):
    return word.replace(" ", "")

assert remove_whitespace("Linus Torvalds") == "LinusTorvalds"
assert remove_whitespace("n vidia is aw ful") == "nvidiaisawful"
assert remove_whitespace("i don't like mentos") == "idon'tlikementos"

def assert_short_name (name):
    assert len(name)<6, "name is too long"
    return f"{name} is a short name"


def average_positives (list):
    for num in list:
        assert num > 0, "not_a positive value"
    average = sum(list)/len(list)
    return average


# EXERCISE 2


# code.interact(local=dict(globals(), **locals()))