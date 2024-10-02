import code 

class Queue (list):
    def isEmpty(self):
        return (len(self) == 0)
    def  enqueue(self, item):
        return self.append(item)
    def dequeue(self):
        assert not(self.isEmpty()), "cannot dequeue from empty list"
        return self.pop(0)
    
class strQueue (Queue):
    def enqueue (self, item):
        assert type(item)== str, "Non string inserted"
        Queue.enqueue (self,item)


class Stack(list):
    def push (self, item):
        return self.append(item)
    def pop (self):
        return  list.pop(self)




code.interact(local=dict(globals(), **locals()))