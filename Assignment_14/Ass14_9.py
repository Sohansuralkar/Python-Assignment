class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __eq__(self,other):
        if isinstance(other,product):
            return self.name == other.name and self.price == other.price
        return False


p1 = product("xyz",1)
p2 = product("xyz",1)
p3 = product("xyzq",2)

print(p1 == p2)
print(p1 == p3)

