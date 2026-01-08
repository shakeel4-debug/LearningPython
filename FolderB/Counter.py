class Counter:
    def __init__(self):
        self.count=0
    def increment(self):
        self.count+=1
    def get_count(self):
        return self.count
    def reset_count(self):
        self.count=0
counter1=Counter()
counter1.increment()
print(counter1.get_count())
counter1.reset_count()
print(counter1.get_count())
counter1.increment()
counter1.increment()
print(counter1.get_count())