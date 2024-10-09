import code 



class BizarroFloat (float):
    def __add__(self,other):
        return float.__sub__(self,other)
    def __sub__(self,other):
        return float.__add__(self,other)
    def __mul__(self,other):
        if other != 0:
            return float.__truediv__(self,other)
    def __truediv__(self,other):
        return float.__mul__(self,other)



class MinQueue(list):
    def enque (self,item):
        self.append(item)
    def dequeue(self):
        min_item = min(self)
        self.remove(min_item)
        return min_item
    def __len__(self):
        return len(self)
    def __repr__(self):
        return str(self)
    def next(self):
        return min(self)
    

class EvenRange:
    def __init__(self, start, end):
        self.__start = start if start % 2 == 0 else start + 1
        self.__end = end if end % 2 == 0 else end - 1

    def __iter__(self):
        return EvenRangeIter(self)


class EvenRangeIter:
    def __init__(self, even_range):
        self.__even_range = even_range
        self.__current = even_range._EvenRange__start

    def __next__(self):
        if self.__current > self.__even_range._EvenRange__end:
            raise StopIteration
        else:
            value = self.__current
            self.__current += 2
            return value

code.interact(local=dict(globals(), **locals()))