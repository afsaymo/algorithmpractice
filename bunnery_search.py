"""A binary search
"""
test_list = [
    1,
    2,
    5,
    9,
    12,
    16,
    19,
    23
]
def bunnery_search(array, search):
    """a binary search given a sorted array and a search element to locate

    Args:
        array (int): a list
        search (int): an element to find in the list
    """
    def get_middle(array):
        """gets the middle indice of the array
        """
        middle = int(len(array) /2)
        return middle

    # we will always be comparing the search element to the middle
    mid = get_middle(array) 
 
    # our exit conditions are either search element found, or we went through the whole list and could not find the element
    while search != array[mid] and len(array) > 1:
        # if the element is smaller than the middle indice value we will search the lower half 
        if search < array[mid]:
            array = array[:mid]
            mid = get_middle(array)
            print(f"Too small", array)
        # if the element is larger than the middle indice value we will search the upper half
        if search > array[mid]:
            array = array[mid:]
            mid = get_middle(array)
            print(f"Too big", array)

    if search == array[mid]:
        print("Element found")
        return True

    if len(array) == 1:
        print("Element not found")
        return False

    
# testing right here because I am too lazy to make an args parser
print(bunnery_search(test_list, 3))

# other conditions to consider:
# Maybe if the graph is THAT big I would include functions for exploring quarters?
# this algorithm has an efficiency of log base 2 complexity