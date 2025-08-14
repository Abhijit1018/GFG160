# Python program to merge K sorted linked lists

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to merge two sorted lists.
def mergeTwo(head1, head2):
    
    # Create a dummy node to simplify 
    # the merging process
    dummy = Node(-1)
    curr = dummy

    # Iterate through both linked lists
    while head1 is not None and head2 is not None:
      
        # Add the smaller node to the merged list
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    # If any list is left, append it to
    # the merged list
    if head1 is not None:
        curr.next = head1
    else:
        curr.next = head2

    # Return the merged list starting
    # from the next of dummy node
    return dummy.next

def mergeListsRecur(i, j, arr):
    
    # If single list is left
    if i == j:
        return arr[i]

    # Find the middle of lists
    mid = i + (j - i) // 2

    # Merge lists from i to mid 
    head1 = mergeListsRecur(i, mid, arr)

    # Merge lists from mid+1 to j 
    head2 = mergeListsRecur(mid + 1, j, arr)

    # Merge the above 2 lists 
    head = mergeTwo(head1, head2)

    return head

# Function to merge K sorted linked lists
def mergeKLists(arr):
    
    # Base case for 0 lists 
    if len(arr) == 0:
        return None

    return mergeListsRecur(0, len(arr) - 1, arr)

def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next

if __name__ == "__main__":
    k = 3

    arr = [None] * k

    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)

    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)

    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)

    head = mergeKLists(arr)

    printList(head)
