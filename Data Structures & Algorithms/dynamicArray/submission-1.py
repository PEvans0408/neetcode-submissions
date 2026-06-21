class DynamicArray:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Dynamic Arrays must have capacity > 0") 
        else: 
            self.capacity = capacity
            self.items = [None for _ in range(self.capacity)]
            self.size = 0

    def get(self, i: int) -> int:
        return self.items[i]

    def set(self, i: int, n: int) -> None:
        self.items[i] = n
        return

    def getSize(self) -> int:
        return self.size

    def resize(self) -> None:
        self.items += [None for _ in range(self.capacity)]
        self.capacity *= 2

    def pushback(self, n: int) -> None:
        if self.capacity == self.getSize(): #If the Dynamic Array is full resize
            self.resize()
        self.items[self.getSize()] = n
        self.size += 1
        
    def popback(self) -> int:
        value = self.items[self.size - 1]
        self.items[self.size - 1] = None
        self.size -= 1
        return value

    def getCapacity(self) -> int:
        return self.capacity