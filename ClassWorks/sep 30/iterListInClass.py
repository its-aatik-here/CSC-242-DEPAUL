class iterSkipList(list):
    'a list that has a reversed, skip iterator'

    def __iter__(self):
        return revListIter(self)

class revListIter(object):
    'the reverse list iterator'

    def __init__(self, lst):
        'create an iterator object for lst'
        self.lst = lst
        self.index = len(lst) - 1

    def __next__(self):
        'return the next element in the list'
        if self.index >= 0: # self.index valid
            val = self.lst[self.index]
            self.index -= 2 
            return val
        else:
            raise StopIteration()
