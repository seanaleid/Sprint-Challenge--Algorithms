# Ingredients:
    # can_move_right()  --> check for the end of the list
    # can_move_left()   --> check for the beginning of the list
    # move_right()      --> moves right
    # move_left()       --> moves left
    # swap()            --> swap what robot is holding for current item in list
    # compare()         --> compares robot's item with current item in list
    # set_light_on()    --> turns on the light ?
    # set_light_off()   --> turns the light off ?
    # light_is_on()     --> checks if the light is on

# Ideas:
    # Use None as a break or stop to come back
    # Start at the beginning and move all the way right, checking items
    # Want to move all large items to the right or all small items ot the right?
        # If I move through the list looking for the the largest items, there's no stop. Works for the first one, but then need to subtract. 
        # If I move through the list looking for the smallest items, I can return to the beginning of the list.
            # Swap smallest item for None, move to the right and repeat. Sorting smallest items to largets, moving left to right. ?? Possible? 
    # Light? --> a booly --> use the light to start/stop a loop? 
    # For loop? for i in l --> No, can't directly call self._list 
    # Use python tutor and small list to practice. 
    

# Method:
    # turn on the light
        # while the light is on, use logic
            # Start at arr[0] and swap items. Robot has 1st item
            # None is inserted into the item's place.

            # First check, can_move_right()
                # Yes 
                    # move_right 
                    # compare()
                        # if robot's item is greater, swap.
                        # don't want to repeat nested loops 
                # No, 
        # turn off light

# Bubble sort works accessing self._list. Breaks a rule.
    # Use a modified bubble sort. 
    # for i in range(len(self._list)-1):
    #     for j in range(0, len(self._list)-i-1):
    #         if self._list[j] > self._list[j+1]:
    #             self._list[j], self._list[j+1] = self._list[j+1], self._list[j]

    # return self._list

# Selection sort uses a variable, breaks a rule.
# loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i --> variable, CANNOT USE
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         # Your code here
#         for j in range(cur_index + 1, len(arr)):
#             if arr[j] < arr[smallest_index]:
#                 smallest_index = j

#         # TO-DO: swap
#         # Your code here
#         arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

#     return arr

