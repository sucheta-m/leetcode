# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.head = None

    def insertAtBegin(self, new_val):
        node = ListNode(new_val)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node

# class Solution:
#     def addTwoNumbers(self, l1, l2):
      


def main():
    l1 = ListNode(val = 1)
    print(l1.val)
    print(l1.next)
    l1.insertAtBegin(2)
    print(l1.val)
    print(l1.next)
    # l2 = ListNode()
    # sol = Solution()
    # sol.addTwoNumbers(l1, l2) 
     
if __name__ == '__main__':
     main()