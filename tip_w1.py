print("Hello, world!")
# hi this is reneca

# Problem 1: Welcome 
def welcome():
    print("Welcome to The Hundred Acre Wood!")

# Problem 6: Double Trouble
# Loop through the array for each index
# multiply the number at each index by 2
def doubled(hunny_jars):
    new_list = []
    for i in range(0, len(hunny_jars)):
        new_number = hunny_jars[i] * 2
        # hunny_jars[i] *= 2
        new_list.append(new_number)
    return new_list

# print(doubled([1,2,3]))
# check if can just use hunny jars?
    
    
def doubled(hunny_jars):
    for i in range(0, len(hunny_jars)):
        hunny_jars[i] *= 2
    return hunny_jars

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

#Problem 7: Poohsticks
# initialize a counter to 0
# loop through the list
# have a counter that checks if it is less than the threshold
#if it is the increment counter
# return the counter.

def count_less_than(race_times, threshold):
    counter = 0
    for i in range(0,len(race_times)):
        if race_times[i]< threshold:
            counter += 1
    return counter

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))

# problem 12: thistle hunt
# init the listIndices
# loop through given list
    # if list[x] == "thistle": 
    # listIndices.append(x)
    
def locate_thistles(items):
    listIndices = []
    for x in range(len(items)):
        if items[x] == "thistle":
            listIndices.append(x)
    
    return listIndices

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))

#Adv Problem 2: Bouncy, Flouncy ... 
#init tigger =1
# loop through the list/array 
# if and elif statements to check if it is either bouncy,flouncy or the others
# increment / decrement based on the value at the index
# return tigger.

def final_value_after_operations(operations):
    tigger = 1
    
    for i in range(0, len(operations)):
        if operations[i] == 'bouncy' or operations[i] == 'flouncy':
                tigger += 1
        elif operations[i] == 'trouncy' or operations[i] == 'pouncy':
                tigger -= 1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))


# Create a stack, add characters 1-by-1 to the stack
# if it is a t, i, gg, or er, do not add
# If we add g, then another, g we can check 2 characters back and remove acdordingly
# Same approach for when adding r, just check the last char to see if it is an e, if it is, remove, do not add r
def tiggerfy(word):
    new_str = []

    for i in range(0, len(word)):
        curr_char = word[i].lower() # ??
        if (curr_char == 't'):
            continue
        elif (curr_char == 'i'):
            continue
         
        # Check er
        elif (curr_char == 'r'):
            if (len(new_str) == 0):
                new_str.append(curr_char)
            else:
                if (new_str[len(new_str) - 1] == 'e'):
                    new_str.pop()
                else:
                    new_str.append(curr_char)
        # Check gg
        elif (curr_char == 'g'):
            if (len(new_str) == 0):
                new_str.append(curr_char)
            else:
                if (new_str[len(new_str) - 1] == 'g'):
                    new_str.pop()
                else:
                    new_str.append(curr_char)
        else:
            new_str.append(curr_char)

    return "".join(new_str)

print(tiggerfy("Trigger"))
print(tiggerfy("eggplant"))
print(tiggerfy("Choir"))


"""
Tr
eplan
Chor
"""

# Forgot about capital letters :( -> currChar.toLower() ?
# -> like T vs t >:(
# nice to work with you!!!
# thank you guys. it was a fu
# Yes it was !!