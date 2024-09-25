class revList(list):
    'a reverse list class'

    def __iter__(self):
        return ListIterator(self)

class ListIterator(object):
    'create an iterator that moves back to front'

    def __init__(self, lst):
        'the constructor for the back-to-front list iterator'
        self.lst = lst
        self.index = len(lst) - 1
        
    def __next__(self):
        'return the next item in the back-to-front list iterator'
        if self.index < 0:
            raise StopIteration()
        res = self.lst[self.index]
        self.index -= 1
        return res
