# Python Program to add two number represented as
# linked list by storing sum on the longer list

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# function to reverse the linked list
def reverse(head):
    prev = None
    curr = head

    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

# function to trim leading zeros in linked list
def trimLeadingZeros(head):
    while head and head.data == 0:
        head = head.next
    return head
  
# Function to find the length of linked list
def countNodes(head):
    length = 0
    curr = head

    while curr is not None:
        length += 1
        curr = curr.next

    return length

# Function to add two numbers represented by linked list
def addTwoLists(num1, num2):
    num1 = trimLeadingZeros(num1)
    num2 = trimLeadingZeros(num2)
    
    # Find the length of both the linked lists
    len1 = countNodes(num1)
    len2 = countNodes(num2)
    
    # If num1 is smaller, swap the two linked lists by 
    # calling the function with reversed parameters
    if len1 < len2:
        return addTwoLists(num2, num1)

    carry = 0
    num1 = reverse(num1)
    num2 = reverse(num2)

    res = num1

    # Iterate till either num2 is not empty or carry is greater than 0
    while num2 is not None or carry != 0:
        # Add carry to num1
        num1.data += carry

        # If num2 linked list is not empty, add it to num1
        if num2 is not None:
            num1.data += num2.data
            num2 = num2.next

        # Store the carry for the next nodes
        carry = num1.data // 10

        # Store the remainder in num1
        num1.data = num1.data % 10

        # If we are at the last node of num1 but carry is
        # still left, then append a new node to num1
        if num1.next is None and carry != 0:
            num1.next = Node(0)

        num1 = num1.next

    # Reverse the resultant linked list to get 
    # the required linked list
    return reverse(res)

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    
    # Creating first linked list: 1 -> 2 -> 3
    # (represents 123)
    num1 = Node(1)
    num1.next = Node(2)
    num1.next.next = Node(3)

    # Creating second linked list: 9 -> 9 -> 9
    # (represents 999)
    num2 = Node(9)
    num2.next = Node(9)
    num2.next.next = Node(9)

    sumList = addTwoLists(num1, num2)
    printList(sumList)
