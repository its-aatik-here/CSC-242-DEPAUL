import code 

class dog:
    def __init__(self,name, age,bark="borf"):
        self.name=name
        self.age=age
        self.bark=bark
    def speak(self):
        print(self.bark)
    def call(self):
        print("Come here, ",self.name)
    def __lt__(self, other):
        return self.age<other.age
    def __eq__(self, other):
        return self.age==other.age
    def __str__(self):
        return "This dogs name is ”+str(self.name) +” and they are “ + str(self.age)+ “ years old."
    def __repr__(self):
        return "dog({},{},{}”.format(self.name,self.age,self.bark)"
    

code.interact(local=dict(globals(), **locals()))
