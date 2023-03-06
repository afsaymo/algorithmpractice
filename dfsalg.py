"""
Created by: Adrianna Saymo
Created on: 1/18/23

The purpose of this program is to exercise Adri's coding skills by implementing a DFS algorithm
This assignment should include
    [\] A DFS search Algorithm
        * a start target
        * an exit target
    [] A BFS search algorithm
        * no Google searching allowed!!
            * sketch the steps yourself :) you can do it!
        * a start target
        * an exit target
    [] A command line args parser for user input
        * the user can select the start and end targets
        * the user can select which search algorithm to use
    [] Turn the command line program into a GUI

    Binary search
    quicksort
    mergesort
    

hurry up with this >:((( 
Check in with someone **twice a week** for feedback and progress

Kenneth suggested watching MCode on YouTube 

"""
import argparse
parsley = argparse.ArgumentParser(description="Sort through a graph using a DFS or BFS search algorithm")
parsley.add_argument("-S","--start", type=str, help="Where the search begins")
parsley.add_argument("-E","--end", type=str, help="Where the search ends")
parsley.add_argument("-D", "--dfs_search", type=str, help="DFS search option")
# parsley.add_argument("-B", "--bfs_search", type=str, help="BFS search option")
args = parsley.parse_args()

graph = {
    'A':['B', 'C'],
    'B':['C', 'D'],
    'C':['D'],
    'D':[]
}
def dfs(graph, start, end):  
    path = []
    stack = [start]
    visted = []
    while(len(stack) !=0):
        s = stack.pop() #
        if s not in path:
            path.append(s)
            visted.append(s) 
        #if s != end:
        for neighbor in graph[s]:   #
            stack.append(neighbor)

        return " ".join(path)   #needs an exit target; if it doesn't find target in an arm it shouldn't be printing the arm it should be cropping the arm
                            #add a visited 
                            #user picks to start and end
                            #option of picking bfs or difs 

"""    
Generate a graph from user input.
For now, we are going to replicate the graph given before we can become more flexible
"""
def main():
    dfs_test = dfs(graph, args.start, args.end)

    print(dfs_test)


if __name__=="__main__":
    main()

    #improvements
    #need start and end; target
    #could be command line program first
    #args parser!!!*
    #docstrings you absolute sandwich go check naludaq*
    #why are you using this function
    #let people read the code
    #make this into a package for gui usage 
    #take graph as a python dictionary 
    #write tests*
    #no recursion >:(
    #inputs req
        #starting
        #target
        #wrong target; return wrong target
        #only small graph; 20 steps
    