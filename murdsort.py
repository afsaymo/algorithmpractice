# how hard is it to make a merge sort algorithm??? very hard. I am crying
# basically we split the array into left and right, sort left, sort right, and then put them together

test_array = [2,8,5,3,4,1,9,6]

def murdsort(array):
    """given an array, we will sort it  using a merge sort

    Args:
        array: list to be sorted
    """
    length = len(array)
    middle = int(length//2)
    
    # base case length <=1
    if length == 1:
        return array
    
    # recursion
    left = array[:middle]
    right= array[middle:]
    
    #merge sort the left side, the right side, and then merge them together
    murdsort(left)
    murdsort(right)
    return murds(left,right,array)
    
def murds(left, right, og):
    """given the left array, right array, and original array
    we sort and copy the left and right into the orignal array

    Args:
        left (list): left half of array
        right (list): right half of array
        og (list): original array to append sorted numbers 
    """
    ltsize = len(left)
    rtsize = len(right)
    l = 0 # left index
    r = 0 # right index
    o = 0 # og index

    # merge left and right
    while(l<ltsize and r<rtsize):
        if(left[l]<right[r]):
            og[o] = left[l]
            l += 1
            o += 1
        else:
            og[o] = right[r]
            r += 1
            o += 1
    
    # add the leftovers
    while l < len(left):
        og[o] = left[l]
        l += 1
        o += 1
    while r < len(right):
        og[o] = right[r]
        r += 1
        o += 1
        
    return og

print(murdsort(test_array))