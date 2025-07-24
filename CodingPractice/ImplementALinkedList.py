# Definition of a ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def remove(self, target):
        """
        Remove a Node, using a target value to find the needed node to remove
        :param target:
        :return:
        """
        pass

    def isCycle(self):
        """
        Cycle within a Linked List
        :return: bool -- True if cycle appears in Linked List
        """
        pass

    def length(self):
        """
        Find the total amount of nodes in a Linked List
        :return: int: number of Nodes in the Linked List
        """
        pass

    def reverse(self):
        """
        Reverse the pointers in the Linked List
        :return: Node: The new head node of the Linked List
        """
        pass

    def stringify(self):
        """
        Produce a string representation of the linked list with arrows for the pointer
        :return: str: 1->2->3->None
        """
        pass

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
