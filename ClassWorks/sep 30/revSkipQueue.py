class revSkipQueue(object):
    'a representation of a queue that skips elements'

    def __init__(self):
        'constructor'
        self.q = list()

    def dequeue(self):
        'removes and returns the item at the front'
        return self.q.pop()

    def enqueue (self, item):
        'adds item to the back of the queue'
        self.q.insert(0, item)

    def size(self):
        'return the number of items in the queue'
        return len(self.q)

    def isEmpty(self):
        'returns True if the queue is empty'
        return self.size() == 0

    def __repr__(self):
        'representation of the queue'
        return f"{self.q}"

    def __str__(self):
        'the string representation of a queue'
        val = ''
        for index in range(len(self.q)-1, -1, -1):
            val += str(self.q[index]) + "\n"
        val = val.strip()
        return val

    def __iter__(self):
        'the iterator'
        return RevSkipListIter(self.q)

class RevSkipListIter(object):
    'the reversed list iterator'

    def __init__(self, lst):
        'the constructor'
        self.lst = lst
        self.index = len(lst) - 1 

    def __next__(self):
        'get the next element'
        if self.index < 0:
            raise StopIteration()
        else:
            item = self.lst[self.index]
            self.index -= 2
            return item

