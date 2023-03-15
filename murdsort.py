# how hard is it to make a merge sort algorithm??? very hard. I am crying
# basically we split the array into left and right, sort left, sort right, and then put them together

test_array = [2,8,5,3,4,1,9,6]

def murdsort(array):
    """given an array, we will sort it  using a merge sort

    Args:
        array (_type_): _description_
    """
    length = len(array)
    middle = int(length/2)
    # base case length <=1
    if length < 1:
        return
    
    left = array[:middle]
    right= array[middle:]
    j = 0

    for i in range(len(array)-1):
        if i<middle:
            left[i] = array[i]
        else:
            right[j]=array[i]
            j+=1

    murdsort(left)
    murdsort(right)
    murds(left,right,array)
    


    print(left)
    print(right)

def murds(left, right, og):
    """given the left array, right array, and original array
    we sort and copy the left and right into the orignal array

    Args:
        left (_type_): _description_
        right (_type_): _description_
        og (_type_): _description_
    """
    size = int(len(og))
    ltsize = size /2 
    rtsize = size - ltsize
    l = 0
    r = 0

    while(l<ltsize and r<rtsize):
        if(left[l]<right[r]):
            og.append(left[l])
            l += 1
        else:
            og.append(right[r])
            o += 1
            l += 1
    # adding leftovers 
    while(l<ltsize):
        og.append(left[l])
        l +=1
    while(r<rtsize):
        og.append(right[r])
        r +=1    


murdsort(test_array)