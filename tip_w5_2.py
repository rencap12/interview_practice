# # class Node:
# #     def __init__(self, value, next=None):
# #         self.value = value
# #         self.next = next

# # # For testing
# # def print_linked_list(head):
# #     current = head
# #     while current:
# #         print(current.value, end=" -> " if current.next else "\n")
# #         current = current.next
# # #understanding: return the maximum, value of linked list and return it
# # #plan: 1. initialize a max_val var to  -inf
# # #2.1 check if list is empty, and r turn none if empty
# # #2.2 transverse through the linked list 
# # #3. if the value of current node is greater than max_val
# # #       then max_val = val of current node
# # # 4. return max_val
# # # since traversing through the list once
# # #time complexity: O(n)
# # #space complexity: o(1)
# # def find_max(head):
# #     max_val = float("-inf") 
# #     if not head:
# #         return None
# #     curr = head
# #     while curr:
# #         if curr.value > max_val:
# #             max_val = curr.value
# #         curr = curr.next
# #     return max_val

# # # head1 = Node(-5, Node(-6, Node(-7, Node(-8))))

# # # # Linked List: 5 -> 6 -> 7 -> 8
# # # print(find_max(head1))

# # # head2 = Node(5, Node(8, Node(6, Node(7))))

# # # # Linked List: 5 -> 8 -> 6 -> 7
# # # print(find_max(head2))

# # #problem2: Remove Tail
# # #understanding: Fix the bug, find the bug and fix it
# # #Plan: Go through the code line by line
# # # O N -> o (1)

# # def remove_tail(head):
# #     if head is None: #for empty list
# #         return None
# #     if head.next is None:  #handles case with a size of 1
# #         print("None")
# #         return None 
        
# #     # current = head
# #     # while current.next.next: 
# #     #     current = current.next

# #     curr = head
# #     prev = head
# #     while curr.next:
# #         prev = curr
# #         curr = curr.next
# #     prev.next = None

    
# #     # current.next = None 
# #     return head

# # head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# # # Linked List: Isabelle -> Alfonso -> Cyd
# # print_linked_list(remove_tail(head))
# # head1 = Node("Isabelle")

# # # Linked List: Isabelle -> Alfonso -> Cyd
# # print_linked_list(remove_tail(head1))

# # print_linked_list(remove_tail(Node("ipkldskfklasjl")))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# #understanding: sorted linked list->just single list
# #plan -  curr = head, dummy prev(handle dups at the beginning), transverse the list loop again through the dupes return prev.next pre
# # dummy = Node()
# # dummy.next = head would   return dummy.next 3 3 4 5 -> 4 5
# # curr = head
# # prev = curr
# #prev.next
# #time complextiy o(n) # we are only visitn  a node once
# #space complexit o(1)



# def delete_dupes(head):
#     temp = Node("temp", head)
#     prev = temp
#     curr = head

#     while curr and curr.next:
#         if curr.value!=curr.next.value:
#             prev = curr
#             curr = curr.next
#         else:
#             repeating = curr.value
#             while curr and curr.value ==repeating:
#                 curr = curr.next # what if curr is none
#             prev.next = curr
#     return temp.next



# head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
# head1 = Node(1, Node(1, Node(3, Node(3, Node(4, Node(5))))))
# head2 = Node(1, Node(1, Node(1, Node(1, Node(1, Node(1))))))



# # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
# print_linked_list(delete_dupes(head))
# print_linked_list(delete_dupes(head1))
# print_linked_list(delete_dupes(head2))


'''
#understanding - given a linked list return true if there is a cycle, false if none
#plan1 - slow and fast pointer (Floyd's algorithm)
#plan2 - using set -- costy space wise

#you either
init a set
iter through LL --> condition curr.next
    add crr to set
    if curr in set return True
if reached LL return False
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    # if not head:
    #     return False
    # seen = set()
    
    # curr = head
    # while curr:
    #     if curr in seen:
    #         return True
    #     seen.add(curr)
    #     curr = curr.next
    # return False

    

    slow = head
    fast = head
    while fast and fast.next:
        slow= slow.next
        fast = fast.next.next
        if slow ==fast:
            return True
    return False
    


peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))