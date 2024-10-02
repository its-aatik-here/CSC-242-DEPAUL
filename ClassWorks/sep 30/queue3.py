# a very simple queue class

class queue(object):
    def __init__(self):
        self.q = []
        
    def dequeue(self):
        return self.q.pop(-1)
    
    def enqueue (self, item):
        return self.q.insert(0, item)
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return (self.size() == 0)
    
    def __repr__(self):
        return self.q.__repr__()
    
    def __str__(self):
        theq = ''
        for index in range(len(self.q)-1, -1, -1):
            theq += str(self.q[index]) + "\n"
        theq = theq.strip()
        return theq
    
    def __getitem__(self, key):
        return self.q[key]
    
    def __setitem__(self, key, value):
        self.q[key] = value
      
    def __iter__(self):
        return QueueIterator(self)

class QueueIterator:
    'iterator for the queue class'
    def __init__(self, q):
        self.index = len(q) - 1
        self.q = q
        
    def __next__(self):
        'return the next queue item'
        if self.index < 0:
            raise StopIteration()
        result = self.q.[self.index]
        self.index -= 1
        return result
