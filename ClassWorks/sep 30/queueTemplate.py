class queue(object):
    
    def __init__(self):
        self.items = []
        
    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueue("cannot dequeue from empty queue")
        return self.items.pop(0)
    
    def enqueue (self, item):
        self.items.append(item)

    def size(self):
        return  len(self.items)
    
    def isEmpty(self):
        return self.size()==0
    
    
    def __repr__(self):
        return str(self.items)
    
    def __str__(self):
        return (self.items)



class EmptyQueue (Exception):
    pass


q = queue()
try:
    q.dequeue()
except EmptyQueue as e:
    print (e)
    
q.enqueue (1)
q.enqueue (2)
print (q.dequeue())
print (q.size())
print (q.isEmpty())