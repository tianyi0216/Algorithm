import sys
from collections import deque

class Node:
    """
    Node class represent a vertex in the flow graph.
    """
    def __init__(self, name, child, capacity):
        self.name = name # name of the vertex
        self.childs = {} # maps child and the capacity of edge node- child
        if child != None and capacity != None:
            self.childs[child] = capacity
    
    def add_child(self, child, capacity):
        """
        Add a child to this node with a specified capacity
        """
        if child in self.childs:
            # if already a child, we just add more capacity - represent extra edge
            self.childs[child] += capacity
        else:
            self.childs[child] = capacity

class Graph:
    """
    Class represents a flow graph with vertices and edges
    """
    def __init__(self):
        # maps node name to their Node object
        self.nodes = {}

    def add_edge(self, edge):
        """
        Adds an edge from std input in the form of [source, dest, capacity]
        """
        source = edge[0]
        dest = edge[1]
        capacity = int(edge[2])

        # if any source or dest are not already in the graph, add first.
        if dest not in self.nodes:
            self.nodes[dest] = Node(dest, None, None)
        if source not in self.nodes:
            self.nodes[source] = Node(source, dest, capacity)
        else:
            # if source already in, add extra child by calling add edge method
            self.nodes[source].add_child(dest, capacity)

    def update_edge(self, parent, child, cost):
        """
        update existing edges during FF algorithm
        """
        # remove the edge is flow is 0
        if cost == 0:
            if child in self.nodes[parent].childs:
                self.nodes[parent].childs.pop(child)
        else:
            self.nodes[parent].childs[child] = cost

    def max_flow(self, target):
        """
        FF algorithm to find the maximum flow
        """
        maxflow = 0
        s = "1"
        t = str(target)
        while True:
            path = self.bfs(s,t)

            # we keep updating until we can't find an augmented path
            if path == None:
                break
            
            # if we found a path, we find the minimum capacity to be our bottleneck
            bottleneck = float("inf")
            for i in range(len(path) - 1):
                if self.nodes[path[i]].childs[path[i+1]] <= bottleneck:
                    bottleneck = self.nodes[path[i]].childs[path[i+1]]
            
            # we can push bottleneck along path - so we add this to the maxflow
            maxflow += bottleneck

            # we update the residual graph, we look at each edge in our path and decide how to update it - see below.
            for i in range(len(path) - 1):
                # forward edge- remove if 0, else add cap-bottleneck.
                cap = self.nodes[path[i]].childs[path[i+1]] 
                self.update_edge(path[i], path[i+1], cap - bottleneck)

                # backward edge - either bottleneck (flow) because that's just f(e) in the algorithm, or we add to existing path's flow already
                if path[i] in self.nodes[path[i+1]].childs:
                    back = self.nodes[path[i+1]].childs[path[i]] + bottleneck
                else:
                    back = bottleneck
                self.update_edge(path[i+1], path[i], back)
                
        return maxflow
            
    def bfs(self, s, t):
        """
        Standard BFS algorithm to find a path from s to t in the graph
        """
        visited = set()
        back = {} # back pointer use to extract path
        todo = deque([s])
        visited.add(s)
        back[s] = None

        # keep exploring while todo has more node to explore
        while len(todo) > 0:
            curr = todo.popleft()
            for child in self.nodes[curr].childs:
                if child == t: # stop early if we found destination
                    back[t] = curr
                    break
                if child not in visited:
                    todo.append(child)
                    visited.add(child)
                    back[child] = curr
        
        # if we can't find destination from starting vertex
        if t not in back:
            return None
        
        # back tracking to get the path
        path = []
        curr = t
        while curr != None:
            path.append(curr)
            curr = back[curr]

        return path[::-1]

        
if __name__ == '__main__': 
    # process input here
    num_instance = int(sys.stdin.readline())
    result = [] # store all result

    # readin data
    for i in range(num_instance):
        node_edge = sys.stdin.readline().strip().split()
        num_node = int(node_edge[0])
        num_edge = int(node_edge[1])
        edges = []
        for i in range(num_edge):
            edges.append(sys.stdin.readline().strip().split())
        
        g = Graph()
        for edge in edges:
            g.add_edge(edge)
        
        result.append(g.max_flow(num_node))
    # print all results
    for res in result:
        sys.stdout.write(str(res) + '\n')