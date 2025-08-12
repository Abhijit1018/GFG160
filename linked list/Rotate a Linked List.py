# Python program to rotate a linked list
# by changing pointer of kth node

class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

# Function to rotate the linked list to the left by k places
def rotate(head, k):

    # If the linked list is empty or no rotations are needed, 
    # return the original linked list
    if k == 0 or head is None:
        return head

    curr = head
    length = 1

    # Find the length of the linked list
    while curr.next is not None:
        curr = curr.next
        length += 1

    # Modulo k with length of linked list to handle
    # large values of k
    k %= length

    if k == 0:
        curr.next = None
        return head

    # Make the linked list circular
    curr.next = head

    # Traverse the linked list to find the kth node
    curr = head
    for _ in range(1, k):
        curr = curr.next

    # Update the (k + 1)th node as the new head
    newHead = curr.next

    # Break the loop by updating the next pointer
    # of kth node
    curr.next = None
    return newHead

def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list: 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    head = rotate(head, 6)
    printList(head)
