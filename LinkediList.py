
# @Creation Date :  04/01/2023
# Description:      LinkedList implementation in Python

class Node:
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next



class LinkedList:
    def __init__(self):
        self.head= None

    def insert(self, data):
        if self.head is None:
            self.head= Node(data)
        else:
            temp=self.head
            while temp.next is not None:
                temp= temp.next
            temp.next= Node(data)

