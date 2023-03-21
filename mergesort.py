"""mergesort 

Created by Adrianna 
3/2/23


Use merge sort to sort arry
takes in one array
"""


test = [8, 2, 5, 3, 4, 7, 6, 1]

# low = [1,3,5]
# high = [2,4,6]
#let's write a merge function first
def merge(left, right, og_array):
    """Given low, middle, and high, we return a list in ascending order

    Args:
        low (int list): _description_
        mid (int list): _description_
        high (int list): _description_
    """
    length = len(og_array)
    leftlen = int(len(og_array)/2)
    rightlen = int(len(og_array) - leftlen)
    l = 0 # index left
    r = 0 # index right

        # if leftlen[l] == rightlen[r]:
        #     og_array.append(leftlen[l])
        #     og_array.append(rightlen[r])
        #     i += 1
        #     r += 1
        #     l += 1

   # merged.extend(low[i:])
    # merged.extend(high[j:])
    return og_array
# print(low)
# print(high)
# print(merge(low, high))

def mergesort(array):
    """given an array, use the merge sort algorith to  return the array sorted"""
    length = len(array)
    # base case, cannot have a list of < 1
    if length <= 1:
        return
    # divide arrays
    middle = int(length/2)
    left = array[:middle]
    right = array[middle+1:]
    i = 0
    j = 0

    for i in range(length):
        if i < middle:
            left.append(array[i])
        else:
            right.append(array[i])
            j +=1
        
        mergesort(left)
        mergesort(right)
        merge(left, right, array)

print(mergesort(test))

   


# def mergesort(array):
#     length = len(array)
#     if length < 1:# base case
#         return
    
#     middle = int(length/2 ) # m for middle
#     left_arr = array[:middle]
#     print(left_arr)
#     right_arr = array[middle:]
#     print(right_arr)
#     l = np.arange(0, length, 1)
#     print(l)
#     r = 0
#     # split arrays 
#     for i in l:
#         if (l[i]<middle):
#             left_arr[i] = array[i]
#         else:
#             right_arr[r] = array[i]
#             r += 1

#     merge(left_arr, right_arr, array)
#     mergesort(left_arr)
#     mergesort(right_arr)


#     return array


# print(mergesort(array))
