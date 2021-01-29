class CountDown:
    def __init__(self, step):
        self.step = step
    
    def __next__(self):
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self

for element in CountDown(4):
    print(element)