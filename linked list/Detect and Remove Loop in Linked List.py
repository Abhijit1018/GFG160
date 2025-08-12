# Python program Using Floyd's Cycle Detection Algorithm

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to remove the loop from the linked list
def removeLoop(head):
  
    # If the list is empty or has only one node 
    # without a loop
    if head is None or head.next is None:
        return

    slow = head
    fast = head

    # Move slow and fast pointers; slow moves 1 step, 
    # fast moves 2 steps
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If slow and fast meet, a loop is detected
        if slow == fast:
            slow = head

            # Move slow and fast pointers to find the node 
            # where the loop starts
            while slow != fast:
                slow = slow.next
                fast = fast.next

            # Traverse the loop to find the node where the 
            # loop ends and remove it
            while fast.next != slow:
                fast = fast.next
            fast.next = None  

def printList(curr):
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()


if __name__ == "__main__":
  
    # Create a linked list:
    # 1 -> 3 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    # Creating a loop 
    head.next.next.next = head.next

    # Remove the loop from the linked list
    removeLoop(head)

    printList(head)
