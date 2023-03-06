"""BFS search
    by adri

    Returns:
        _type_: _description_
    """
from collections import defaultdict
graph = {
        'A':['B', 'C'],
        'B':['C', 'D'],
        'C':['D'],
        'D':[]
    }


def breakfast_search(graph, start, end):
    explored = defaultdict(bool) 
    explored[start] = True
    barbieq = []
    barbieq.append(start)

    while explored[end] == False: #is checks if its the same object; this is dangerous;
        #bool is okay though because there's only one True and one False 
        s = barbieq.pop(0) # look at the first element in queue
        #while end not in explored:
            #explore all of the first element first! Look for all the neighbors
        for neighbor in graph[s]: #look at all of the neigbors in this node
            if explored[neighbor] == False: #check if explored
                explored[neighbor] = True #neighbor gets explored
                barbieq.append(neighbor) #add the neighbor to our queue S
    return explored

print(breakfast_search(graph, 'B', 'D')) #how to prune this path; does not print nicely :L

#does not work for non cyclic graphs!! 
#dfs can find cycles
#need edge conditions
#remember what Big O is!! 
#array, stack, linked list, queue
#figure out how to use hash map!! 
#set; implemented under the hood with a hash map (with Booleans in C) 
#dictdict[bool]
