# Problem 1
def count_layers(sandwich):
    # Understand: given layered list -> how many layers
    # Edge: empty list -> 0; must have stuff to be a layer
    # ["bread", []] -> 1;
    # Plan -> for each layer if one of the elements is a list -> call max again on each those return max of depths
    # ["b", [], []]
    # return max[1] [2]

    if not sandwich or type(sandwich) != list:
        return 0

    add = 0
    max_value = float('-inf')
    for part in sandwich:
        max_value = max(max_value, count_layers(part))
        if type(part) != list:
            add = 1

    
    return add + max_value


sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
sandwich3 = [] # 0
sandwich4 = ["bread", ["cheese"], ["lettuce", ["meat"]]] # 3
sandwich5 = [["bread", "cheese", "lettuce"], ["meat", "salami", "chicken"]]
sandwich6 = [[[]]] # 0

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))
# print(count_layers(sandwich3))
# print(count_layers(sandwich4))
# print(count_layers(sandwich5))
# print(count_layers(sandwich6))

#orders_new = " ".join(orders_split[:-1])

def reverse_orders(orders):
    orders_split = orders.split(" ")
    if not orders_split:
        return ""
    if len(orders_split) == 1:
        return orders_split[0]

    orders_new = " ".join(orders_split[:-1])
    return orders_split[-1] + " " +  reverse_orders(orders_new)
    
#print(reverse_orders("Bagel Sandwich Coffee"))


# Problem 3 Sharing the Coffee
def can_split_coffee(coffee, n):
    """
    return a bool if total volume found % n == 0
    
    def getVolume(coffee):
        if not coffee:
            return 0
        take first elem available + recurr to the rest of coffee
            return coffee[0] + getVolume(cofee[1:])
        
    
    return val % n == 0
    """
    def getVolume(coffee):
        if not coffee:
            return 0
        return coffee[0] + getVolume(coffee[1:])

    val = getVolume(coffee)
    
    return val % n == 0

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
