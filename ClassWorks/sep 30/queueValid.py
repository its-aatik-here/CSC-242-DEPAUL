class queue(object):
    def __init__(self):
        'the constructor'
        self.q = list()
        
    def dequeue(self):
        'removes and returns the first item in the queue'
        assert self.isEmpty() == False, f"Cannot dequeue from an empty queue"
        return self.q.pop(0)
    
    def enqueue(self, item):
        'add item to the back of the queue'
        self.q.append(item)
    
    def size(self):
        'returns the number of items in the queue'
        return len(self.q)
    
    def isEmpty(self):
        'return True if the queue is empty'
        return self.size() == 0
    
    def __repr__(self):
        'the representation'
        return repr(self.q)
    
    def __str__(self):
        'the string representation'
        theq = ''
        for index in range(len(self.q)):
            theq += str(self.q[index]) + "\n"
        theq = theq.strip()
        return theq

    def __iter__(self):
        'the iterator'
        return iter(self.q)
