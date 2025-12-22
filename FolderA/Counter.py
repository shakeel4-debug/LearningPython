class Counter:
    def __init__(self):
        self.count=0
    def increment(self):
        self.count+=1
    def get_count(self):
        return self.count
    def reset(self):
        self.count=0
counter1=Counter()
counter2=Counter()
counter1.increment()
counter2.increment()
counter1.increment()
print(f"Counter 1: {counter1.get_count()}")
print(f"Counter 2: {counter2.get_count()}")