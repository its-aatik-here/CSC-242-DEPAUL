class queue(object):
    
    def __init__(self):
        self.q = []
        
    def dequeue(self):
        assert not(self.isEmpty()),"Cannot Dequeue from empty queue"
        #return self.q.pop(0)
        return self.q.pop()
    
    def enqueue (self, item):
        self.q.insert(0,item)
        #self.q.append(item)
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return self.size()<=0
    
    def __repr__(self):
        return f"queue({str(self.q)})"
    
    def __str__(self):
        return f"entrace: {str(self.q)} :exit"

    def __iter__(self):
        return q_iterator(self.q)

class q_iterator:
    def __init__(self,in_queue):
        self.queue = in_queue
        self.index =0
    def __next__(self):
        if self.index <self.queue.size():
            res = self.queue[self.index]
            self.index+=1
            return res
        else:
            raise StopIteration
class q_iterator_skips:
    def __init__(self,in_queue):
        self.queue = in_queue
        self.index =0
    def __next__(self):
        if self.index <self.queue.size():
            res = self.queue[self.index]
            self.index+=2
            return res
        else:
            raise StopIteration 
        

class q_iterator_rev:
    def __init__(self,in_queue):
        self.queue = in_queue
        self.index = len(in_queue)
    def __next__(self):
        if self.index-1<0:
            raise StopIteration
        self.index-=1
        return self.queue[self.index]

class my_list_iterator:
    def __init__(self,lst):
        self.lst=lst
        self.index = len(lst)-1
    def __next__(self):
        if self.index<0:
            raise StopIteration
        self.index -=1
        return self.lst[self.index+1]
