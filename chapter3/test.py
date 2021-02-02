class A:
    def __init__(self):
        print("A", end=" ")
        super().__init__()

class C():
    def __init__(self):
        print("C", end=" ")
        


print("MRO:", [x.__name__ for x in C.__mro__])
C()