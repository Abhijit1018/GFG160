# Iterative Python program to reverse a linked list
class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

# Given the head of a list, reverse the list and return the
# head of reversed list
def reverseList(head):

    # Initialize three pointers: curr, prev and next
    curr = head
    prev = None

    # Traverse all the nodes of Linked List
    while curr is not None:

        # Store next
        nextNode = curr.next

        # Reverse current node's next pointer
        curr.next = prev

        # Move pointers one position ahead
        prev = curr
        curr = nextNode

    # Return the head of reversed linked list
    return prev

def printList(node):
    while node is not None:
        print(f" {node.data}", end="")
        node = node.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    printList(head)

    head = reverseList(head)

    print("Reversed Linked List:", end="")
    printList(head)
