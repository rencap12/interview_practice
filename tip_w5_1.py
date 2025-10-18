# # class Villager:
# #     def __init__(self, name, species, personality, catchphrase):
# #         self.name = name
# #         self.species = species
# #         self.catchphrase = catchphrase
# #         self.personality = personality
# #         self.furniture = []
    
# #     def add_item(self, item_name):
# #         self.furniture.append(item_name)

# #     def __str__(self):
# #         return f"{self.name} the {self.species} ({self.personality})"


# # def of_personality_type(townies, personality_type):
# #     names = []
# #     for x in townies:
# #         print(x)  # This automatically calls x.__str__()
# #         if x.personality == personality_type:
# #             names.append(x.name)
# #     print(names)
# #     return names


# # # --- test code below ---
# # isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# # bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# # stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# # print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# # print(of_personality_type([isabelle, bob, stitches], "Cranky"))


# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next

# def catch_fish(head):
#     if not head:
#         print("Aw! Better luck next time!")
#         return None

#     caught = head.fish_name
#     print(f"I caught a {caught}!")
    
#     head = head.next
#     return head

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))