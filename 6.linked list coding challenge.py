class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
        
    def print_list(self):
        temp = self
        while temp:
            print(temp.val, end = " ")
            temp = temp.next

def reverse_every_k_elements(head: Node, k: int)-> Node:
    if k <= 1 or not head:
        return head
    
    prev, curr = None, head
    while True:
        last_node_prev_part = prev
        last_node_sub_list = curr
        
        i = 0
        later = None
        while curr and i < k:
            later = curr
            curr = curr.next
            later.next = prev
            prev = later
            i += 1
            
        if last_node_prev_part:
            last_node_prev_part.next = prev
        else:
            head = prev
        
        last_node_sub_list.next = curr
        
        i = 0
        while curr and i < k:
            prev = curr
            curr = curr.next
            i += 1
        
        if not curr:
            break
    return head

def rotate_list_by_k(head: Node, k: int)-> Node:
    if not head or k <= 0:
        return head
    length = 1
    curr = head
    while curr.next:
        curr = curr.next
        length += 1
    curr.next = head
    
    # no need to rotate length
    k = k%length
    skip_length = length - k
    last_node = head
    for i in range(skip_length-1):
        last_node = last_node.next
    head = last_node.next
    last_node.next = None
    return head
    

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    print("")
    k = 3
    print("k=", k)
    result = reverse_every_k_elements(head, k)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
    print("")
    
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    print("")
    result = rotate_list_by_k(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
