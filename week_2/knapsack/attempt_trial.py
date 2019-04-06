
class Trial:

    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def run(self):
        value = 0
        weight = 0
        taken = [0]*len(self.items)

        for item in self.items:
            if weight + item.weight <= self.capacity:
                taken[item.index] = 1
                value += item.value
                weight += item.weight
        
        return (taken, value)