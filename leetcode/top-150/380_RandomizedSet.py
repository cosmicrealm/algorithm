import random
class RandomizedSet:

    def __init__(self):
        self.context = []
        self.pos = {}
        
    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.context.append(val)
        self.pos[val] = len(self.context)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        self.context.pop(self.pos[val])
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.context)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()