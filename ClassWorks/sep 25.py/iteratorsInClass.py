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
            self.index -= 1 
            return val
        else:
            raise StopIteration()
        
class listIter(object):
    'the regular list iterator for pedagogical purposes'

    def __init__(self, lst):
        'create an iterator object for lst'
        self.lst = lst
        self.index = 0

    def __next__(self):
        'return the next element in the list'
        if self.index <= len(self.lst)-1: # self.index valid
            val = self.lst[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration()
