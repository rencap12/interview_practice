# hi this is reneca

# Problem 1

'''
You are organizing a prestigious event, and you must arrange the order in which guests arrive based on a set of instructions.

The instructions are provided as a 0-indexed string arrival_pattern of length n, consisting of the characters:

'I' - The next guest should have a higher number than the previous guest.
'D' - The next guest should have a lower number than the previous guest.
You need to create a string guest_order of length n + 1 that satisfies the following conditions:

guest_order contains each number from 1 to str(n + 1) exactly once. These numbers represent the guests' assigned numbers.
For every index i from 0 to n - 1:
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Among all valid orders, return the lexicographically smallest one.

I -> Increasing
D -> Decreasing

Stack based approach may be beneficial, numeric disparities occur at differences of I and D

strictly increasing
stack = [1,2,3,4]
4,3,2,1


"IIIDIDDD"
counter = 5
stack = []
output = [1,2,3, 5, 4]
'''
def arrange_guest_arrival_order(arrival_pattern):
    #Initialize result array, and stack
    stack = ["1"]
    result = []

    #Loop through our arrival pattern
    for i in range(2, len(arrival_pattern) + 2):
        if arrival_pattern[i - 2] == "I":
            while stack:
                result.append(stack.pop())
        stack.append(str(i))
        
    #Final stack emptying
    while stack:
        result.append(stack.pop())

    #Return the joined string
    return "".join(result)

print(arrange_guest_arrival_order("IIIDIDDD")) #123549876
print(arrange_guest_arrival_order("DDD")) #  4321
print(arrange_guest_arrival_order("DIDDD")) # 216543


'''You are planning a special event where each attendee has a unique registration number. 
These numbers are listed in the provided array attendees, but they are currently out of order.

At the event, attendees will walk on stage one by one following this special reveal process:

The person at the front of the line walks on stage (this number is revealed).
If there are still people left in line, the next person in front moves to the back of the line.
Steps 1 and 2 repeat until everyone has walked on stage.
Your task is to rearrange the attendees list before the process starts so that the attendees walk on stage by registration number in increasing order.

Write a function reveal_attendee_list_in_order(attendees) that returns an array with the correct starting order, 
such that when the attendees follow the above reveal process they walk on stage from smallest registration number 
to largest registration number.


[17,13,11,2,3,5,7]
[2, 3, 5, 7, 11, 13, 17] # RAHHHHHHHHHHHHH lmao i will continue this somehow



sort the input then simulate the process in reverse
1. start with max
2. append next max to the end of the queue
3.


[1, 1000, 50]
sorted = [1, 50, 100]
          l       r
queue = [1]
queue = []

'''