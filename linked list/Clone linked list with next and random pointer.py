# Python code to Clone a linked list with next and random
# pointer by Inserting Nodes In-place

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None

# Function to clone the linked list
def cloneLinkedList(head):
    if head is None:
        return None
    
    # Create new nodes and insert them next to 
    # the original nodes
    curr = head
    while curr is not None:
        newNode = Node(curr.data)
        newNode.next = curr.next
        curr.next = newNode
        curr = newNode.next
    
    # Set the random pointers of the new nodes
    curr = head
    while curr is not None:
        if curr.random is not None:
            curr.next.random = curr.random.next
        curr = curr.next.next
    
    # Separate the new nodes from the original nodes
    curr = head
    clonedHead = head.next
    clone = clonedHead
    while clone.next is not None:
        # Update the next nodes of original node 
        # and cloned node
        curr.next = curr.next.next
        clone.next = clone.next.next
        
        # Move pointers of original as well as  
        # cloned linked list to their next nodes
        curr = curr.next
        clone = clone.next
    curr.next = None
    clone.next = None
    
    return clonedHead

# Function to print the linked list
def printList(head):
    while head is not None:
        print(f"{head.data}(", end="")
        if head.random:
            print(f"{head.random.data})", end="")
        else:
            print("null)", end="")
        
        if head.next is not None:
            print(" -> ", end="")
        head = head.next
    print()

if __name__ == "__main__":
  
    # Creating a linked list with random pointer
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head.next
    
    # Print the original list
    print("Original linked list:")
    printList(head)
    
    # Function call
    clonedList = cloneLinkedList(head)
    
    print("Cloned linked list:")
    printList(clonedList)
