# Python3 program to return first node of loop.

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def findFirstNode(head):
  
    # Initialize two pointers, slow and fast
    slow = head
    fast = head
    
    # Traverse the list
    while fast and fast.next:
      
        # Move slow pointer by one step
        slow = slow.next
        
        # Move fast pointer by two steps
        fast = fast.next.next
        
        # Detect loop
        if slow == fast:
          
            # Move slow to head, keep
            # fast at meeting point
            slow = head
            
            # Move both one step at a time until
            # they meet
            while slow != fast:
                slow = slow.next
                fast = fast.next
                
            # Return the meeting node, which is the 
            # start of the loop
            return slow
    
    # No loop found
    return None

# Create a linked list: 10 -> 15 -> 4 -> 20
head = Node(10)
head.next = Node(15)
head.next.next = Node(4)
head.next.next.next = Node(20)

head.next.next.next.next = head

loopNode = findFirstNode(head)

if loopNode:
    print(loopNode.data)
else:
    print(-1)
