class Node:
    def __init__(self, data, nxt):
        self.data = data
        self.nxt = nxt

class LinkedList:
    def __init__(self):
        self.dumTail = Node(data=None, nxt=None)
        self.dumHead = Node(data=None, nxt=self.dumTail)

    def get(self, index: int) -> int:
        current = self.dumHead
        for _ in range(index + 1):
            current = current.nxt
            if current == self.dumTail or current.nxt == None:
                return -1
        return current.data
            
    def insertHead(self, data: int):
        s = Node(data, nxt=self.dumHead.nxt)
        self.dumHead.nxt = s

    def insertTail(self, data):
        self.dumTail.data, self.dumTail.nxt = data, Node(data=None, nxt=None)
        self.dumTail = self.dumTail.nxt

    def remove(self, index: int) -> bool:
        if self.dumHead.nxt == self.dumTail:
            return False
        current = self.dumHead #Make sure u dont have issues w removing head
        for _ in range(index):
            current = current.nxt
            if current.nxt == self.dumTail:
                return False
        current.nxt = (current.nxt).nxt
        return True

    def getValues(self) -> List[int]:
        L = []
        current = self.dumHead.nxt
        while current.nxt:
            if current != self.dumTail:
                L.append(current.data)
                current = current.nxt
            else: break
        return L