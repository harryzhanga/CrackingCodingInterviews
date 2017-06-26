class Node:
    #my implementation of a node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        
def print_list(lst):
    curr = lst.head
    while curr != None:
        print(curr.data)
        curr = curr.next

def add_to_tail(lst, data):
    new_node = Node(data)
    if lst.head == None:
        lst.head = new_node
        lst.tail = new_node
        return
    lst.tail.next = new_node
    lst.tail = new_node
    return

def create_list(datas):
    lst = LinkedList()
    for elem in datas:
        add_to_tail(lst, elem)
    return lst


def get_len(lst):
    length = 0
    curr = lst.head
    while curr != None:
        length += 1
        curr = curr.next
    return length

def get_nth_last(lst, n):
    #naive method, run through array twice. O(n)
    list_length = get_len(lst)
    index = list_length - n
    curr  = 0
    curr_node = lst.head
    while curr != index:
        curr_node = curr_node.next
        curr += 1
    return curr_node.data

my_list = create_list([1, 4, 2, 6, 2, 5])
