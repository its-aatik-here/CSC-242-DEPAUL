class queue(object):
    
    def __init__(self):
        self.q = []
        
    def dequeue(self):
        assert not (self.isEmpty()), "cannot deque for empty list"
        #return self.q.pop()
        return  self.q.pop()
    def enqueue (self, item):
        self.q.insert (0,item)

    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return self.size()<=0
    
    def __repr__(self):
        return f"queue ({str(self.q)})"
    
    def __str__(self):
        return  f"enterance: ({str(self.q)}) :exit"

    def __iter__(self):
        return q_iterator(self.q)

class  q_iterator:
    def __init__(self, in_queue):
        self.q = in_queue
        self.index = 0
    def  __next__(self):
        if self.index-1 <0:
            raise StopIteration
        self.index -=1
        return self.index
        # if self.index >= 0:
        #     res = self.queue [self.index]
        #     self.index += 1
        #     return res
        # else:
        #     raise StopIteration
class q_iterator_skips:
    def __init__(self, in_queue):
        self.q = in_queue
        self.index = 0
    def   __next__(self):
        if self.index <self.queue.size():
            res = self.queue[self.index]
            self.index += 2
            return res
        else:
            raise StopIteration

class my_list_iterator:
    def  __init__(self, lst):
        self.lst = lst
        self.index = len(lst)-1
    def __next__ (self):
        if self.index<0:
            raise StopIteration