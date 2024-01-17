# Definition for singly-linked list.
import math

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head 
        print(self.head)
        while (temp): 
            print (temp.val, " -> ", end = '') 
            print(temp.next)
            temp = temp.next
        print("")

    def insertAtBegin(self, new_val):
        node = Node(new_val)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        node1 = Node()
        node2 = Node()
        node1.next = l1.head
        node2.next = l2.head
        node1 = node1.next
        node2 = node2.next

        l3 = LinkedList()
        while ((node1.next != None and node2.next != None) or carry != 0):
            sum = node1.val + node2.val
            if math.floor(sum/10) != 0:
                sum = sum%10
                carry = math.floor(sum/10) + carry
            l3.insertAtBegin(sum)
            node1 = node1.next
            node2 = node2.next

        #run once more
        sum = node1.val + node2.val
        if math.floor(sum/10) != 0:
            sum = sum%10
            carry = math.floor(sum/10) + carry
        l3.insertAtBegin(sum)

        #reverse list
        prev = None
        current = l3.head
        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        l3.head = prev
        return l3

def main():
    l1 = LinkedList()
    l1.insertAtBegin(2)
    l1.insertAtBegin(4)
    l1.insertAtBegin(5)
    l1.printList()
    l2 = LinkedList()
    l2.insertAtBegin(3)
    l2.insertAtBegin(1)
    l2.insertAtBegin(2)
    l2.printList()
    sol = Solution()
    ans = sol.addTwoNumbers(l1, l2) 
    ans.printList()
     
if __name__ == '__main__':
     main()
