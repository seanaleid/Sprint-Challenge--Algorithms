'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Initialize a count
    count = 0
    # Base case
    # If the word is less than the length of 2,
    # it can't be "th", so return the count.
    if len(word) < 2:
        return count
    # Otherwise (all other cases).
    else:
        # If the characters at positions 0 and 1
        # equal "th", increment the counter,
        # return the counter, and recursively call
        # the function slicing the word from position 2
        # until the end.
        if word[0:2] == "th":
            count+=1
            return count + count_th(word[2:])
        # Otherwise, recursively call the function and pass
        # the parameter of the word sliced from position 1 
        # to the end. 
        else:
            return count_th(word[1:])
    
