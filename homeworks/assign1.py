# import code 

#EXERCISE 1

def remove_whitespace (word):
    return word.replace(" ", "")

assert remove_whitespace("Linus Torvalds") == "LinusTorvalds"
assert remove_whitespace("n vidia is aw ful") == "nvidiaisawful"
assert remove_whitespace("i don't like mentos") == "idon'tlikementos"

def assert_short_name (name):
    if len(name)<6:
        return f"{name} is a short name"
    else:
        return "error"

assert_short_name ("linus") == "linus is a short name"
assert_short_name ("aatik") == "aatik is a short name"
assert_short_name ("aatikali") == "error"

def average_positives (list):
    for num in list:
        assert num > 0, "not_a positive value"
    average = sum(list)/len(list)
    return average

assert average_positives([1,1,1,1]) == 1
assert average_positives([1,2,3,4,5]) == 3
assert average_positives([1,2,3,-1]) == "not_a_positive_value"
    


# code.interact(local=dict(globals(), **locals()))