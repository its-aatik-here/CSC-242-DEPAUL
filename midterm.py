'''
Problem 1
Song Class
'''

class Song:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def __str__(self):
        return f"{self.title} by {self.artist} - {self.duration} seconds"

    def __repr__(self):
        return f"Song('{self.title}', '{self.artist}', {self.duration})"

    def __eq__(self, other):
        return self.artist == other.artist

    def __lt__(self, other):
        return self.duration < other.duration

    def __len__(self):
        return self.duration





'''
Problem 2
Double Stack
'''
class DoubleStack(list):
    def push_left(self, item):
        self.insert(0, item)   # insert at the beginning of the list

    def push_right(self, item):
        self.append(item)       # append to the end of the list

    def pop_left(self):
        if not self:
            raise IndexError("pop from an empty list")
        return self.pop(0)       # remove and return the first item

    def pop_right(self):
        if not self:
            raise IndexError("pop from an empty list")
        return self.pop()          # remove and return the last item

    def is_empty(self):
        return not self

    def size(self):
        return len(self)





'''
Problem 3 
SafeDoubleStack with Class Invariants
'''

class SafeDoubleStack(DoubleStack):
    def __init__(self, max_size=float('inf')):
        DoubleStack.__init__(self)
        self.max_size = max_size

    def push_left(self, item):
        assert len(self) < self.max_size, f"Stack cannot exceed the maximum size of {self.max_size}."
        self.insert(0, item)

    def push_right(self, item):
        assert len(self) < self.max_size, f"Stack cannot exceed the maximum size of {self.max_size}."
        self.append(item)

    def pop_left(self):
        assert not self.is_empty(), "Cannot pop from the left side of an empty stack."
        return self.pop(0)

    def pop_right(self):
        assert not self.is_empty(), "Cannot pop from the right side of an empty stack."
        return self.pop()



    
'''
Problem 4 
StringRange Class
'''


class StringRange:
    def __init__(self, string, step=1):
        assert type(step) == int and step > 0, "Step size must be a positive integer."
        self.string = string
        self.step = step

    def __iter__(self):
        return StringRangeIterator(self.string, self.step)


class StringRangeIterator:
    def __init__(self, string, step):
        self.string = string
        self.step = step
        self.index = 0

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        char = self.string[self.index]
        self.index += self.step
        return char