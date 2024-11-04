class Clicker:
    def __init__(self):
        self.clicks = 0
    def press(self,count = 1):
        self.clicks+= count
    def clear(self):
        self.clicks=0
    def get_total(self):
        return self.clicks
