class Node:
    #my implementation of a node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #implementation of a linked list
    def __init__(self):
        self.tail = None
        self.head = None
        
def print_list(lst):
    """Prints out the data of the list"""
    curr = lst.head
    while curr != None:
        print(curr.data)
        curr = curr.next

def add_to_tail(lst, data):
    """Appends a new node with data to the end of a singly linked list"""
    new_node = Node(data)
    if lst.head == None:
        lst.head = new_node
        lst.tail = new_node
        return
    lst.tail.next = new_node
    lst.tail = new_node
    return

def create_list(datas):
    """Create a list based off the array or some other iterable data structure"""
    lst = LinkedList()
    for elem in datas:
        add_to_tail(lst, elem)
    return lst


def get_len(lst):
    """Returns the number of nodes in the singly linked list, assuming not circular"""
    length = 0
    curr = lst.head
    while curr != None:
        length += 1
        curr = curr.next
    return length

#2.2
def get_nth_last(lst, n):
    """Get the nth last node in the linked list"""
    #naive method, run through array twice. O(n)
    list_length = get_len(lst)
    index = list_length - n
    curr  = 0
    curr_node = lst.head
    while curr != index:
        curr_node = curr_node.next
        curr += 1
    return curr_node.data

#2.3
def delete_middle(middlenode):
    """Given a middlenode or any node of the linked list, alter the data so that is appears deleted"""
    if not middlenode:
        return
    if not middlenode.next:
        middlenode.data = None
        return
    middlenode.data = middlenode.next.data
    middlenode.next = middlenode.next.next
    return
    
#2.4
def add_lists(lst1, lst2):
    """given two lists denoting numbers backwards, create a new linked list that contains the sum of those two"""
    #iterative solution
    newlist = LinkedList()
    lst1_node = lst1.head
    lst2_node = lst2.head
    carryover = 0
    while lst1_node or lst2_node:
        number = carryover
        if lst1_node:
            number += lst1_node.data
            lst1_node = lst1_node.next
        if lst2_node:
            number += lst2_node.data
            lst2_node = lst2_node.next
        if number >= 10:
            number = number - 10
            carryover = 1
        else:
            carryover = 0
        add_to_tail(newlist, number)
    if carryover:
        add_to_tail(newlist, 1)
    return newlist

def add_lists_2_use(lst1, lst2):
    """Another method"""
    newlist = LinkedList()
    newnode = Node(None)
    newlist.head = add_lists_2(lst1.head, lst2.head, 0, newnode)
    return newlist

def add_lists_2(node1, node2, carry, curr_node):
    """Recursive solution to the adding lists problem"""
    if not node1 and not node2:
        if carry:
            return Node(1)
        return None
    digit = carry
    if node1:
        digit += node1.data
        node1 = node1.next
    if node2:
        digit += node2.data
        node2 = node2.next
    if digit >= 10:
        digit -= 10
        carry = 1
    else: 
        carry = 0
    newnode = Node(None)
    curr_node.data = digit
    curr_node.next = add_lists_2(node1, node2, carry, newnode)
    return curr_node


#2.5
def circular_Start(lst):
    """If the linked list is circular, find the start of the loop, otherwise return False"""
    if not lst.head:
        return False

    slow = lst.head
    fast = lst.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if not fast or fast.next:
        return False
    
    #at this point, slow and fast have found each other
    
    #by the logic in the book, this should work. But the mathemtics is still a little fuzzy
    slow = lst.head
    while slow != fast:
        #they will meet each other at the start of the loop
        slow = slow.next
        fast = fast.next
    return slow

















