class Node:  
    def __init__(self, value=0):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index+1): 
            curr = curr.next  
            if curr == None:
                return -1        
        return curr.value
                 
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)


    def addAtTail(self, val: int) -> None:
        curr = self.head
        newnode = Node(val)
        while curr.next != None:
            curr = curr.next
        curr.next = newnode


    def addAtIndex(self, index: int, val: int) -> None:
        newnode = Node(val)
        curr = self.head

    
        for i in range(index):
            curr = curr.next

            if curr == None:
                return 
        newnode.next = curr.next
        curr.next = newnode 

    def deleteAtIndex(self, index: int) -> None:
        newnode = Node()
        curr = self.head
        for i in range(index):
            curr = curr.next

            if curr == None:
                return
        if curr.next != None:
            curr.next = curr.next.next


#def __str__(self):
#    arr = [self.value]
#    temp = self.next
#    while temp:
#       arr.append(temp.value)
#    return '->'.join(arr)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)