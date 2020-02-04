#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    
    # check if item is in array
    if array[index] == item:
        return index
    # if item is not in array retun NONE
    if index == len(array) -1 and array[index] != item:
        return None
    index += 1
    return linear_search_recursive(array, item, index)

    # save the index to a variable 
    # create a condition to check if array[index] == item 
    # if yes return index 
    #otherwise call the function again and update the index 
    # create another condition to check if the index is at the last item in  the list 
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # # implement binary_search_iterative and binary_search_recursive below, then
    # # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    # Sort the array
    array = sorted(array)

    # set the left value to the first index of the list which is zero
    left = 0 

    # set the right to the last index in the array
    right = len(array) - 1

    while left <= right:
       
       # get the middle index of the array
        middle_value = (left + right) // 2

        # if the middle value is less than item than move to the left index to the right  once 
        if array[middle_value] < item:
           left = middle_value + 1
        # if the item is greater than the middle index move the right to the left once  
        if array[middle_value] > item:
           right = middle_value - 1
        # if the middle value == the target value return the middle value index 
        if array[middle_value] == item:
            return middle_value
    # if the item is not in the array return NONE
    return None


    
    # reasign array to sorted array 
    # only sort once 

    # create a variable named median and set it to int(len(array) / 2)


    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # Sort the array
    array = sorted(array)


    # get the middle index of the array
    if left == None and right == None:
        left = 0
        right = len(array) -1
    
    
    middle_value = (left + right) // 2

    print('MIDDLE VALUE', middle_value)
        
    if left > right:
        return None

    # if the middle value == the target value return the middle value index 
    if array[middle_value] == item:
        print('---MIDDLE Value ---',middle_value)
        return middle_value

    # if the middle value is less than item than move to the left index to the right  once 
    if array[middle_value] < item:
        left = middle_value + 1
        print('---LEFT----', left)
        return binary_search_recursive(array, item, left, right)

    
    # if the item is greater than the middle index move the right to the left once  
    if array[middle_value] > item:
        right = middle_value - 1
        print('----RIGHT 1----', right)
        return binary_search_recursive(array, item, left, right)

    
    


    

    
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


