# A very simple queue class that could use some doc strings

class queue(object):
    def __init__(self):
        self.q = []
        
    def dequeue(self):
        return self.q.pop(0)
    
    def enqueue (self, item):
        return self.q.append(item)
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return (self.size() == 0)
    
    def __repr__(self):
        return repr(self.q)
    
    def __str__(self): 
        theq = ''
        for index in range(len(self.q)):
            theq += str(self.q[index]) + "\n"
        theq = theq.strip()
        return theq
##    
##    # Ignore what follows for now
##    def __getitem__(self, key):
##        return self.q[key]
##    def __setitem__(self, key, value):
##        self.q[key] = value
##    def __iter__(self):
##        return iter(self.q)

