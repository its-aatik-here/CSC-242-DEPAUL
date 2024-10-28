def str_to_list(str1):
    return list(str1)

def makeExcited(dull_str):
    res = dull_str.replace('.','!')
    return res

def double_evens(lst):
    for i in range(len(lst)):
        if lst[i]%2 == 0:
            lst[i] = lst[i]*2
    return lst






if __name__ == "__main__":
    print(str_to_list('hey'))
    print(str_to_list('there'))
    print(str_to_list('delilah'))
    
    print(makeExcited('hey guys.'))
    print(makeExcited('its tuesday.'))
    print(makeExcited('Do not like mentos.'))
    
    print(double_evens([1,2,3,4,5,6]))
    print(double_evens([0,10,100,-2,6,8]))
    print(double_evens([-1,-2,-3]))


