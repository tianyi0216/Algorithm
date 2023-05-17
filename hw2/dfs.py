class Graph:
    """
    Class represents a graph object to perform dfs on
    """

    def __init__(self, nodenames):
        self.nodes = {} # dictionary map name (value) of a node to a node object
        self.order = [] # order to store the result from a search
        self.visited = set() #set of all visited node already
        self.nodenames = nodenames # list of all possible nodes not searched yet

    def add_node(self, node):
        """
        Add an extra node to the graph
        """
        self.nodes[node.name] = node

    def dfs(self, node):
        """
        DFS method, with run time O(m+n) where m is num of edge and n is num of nodes
        """

        # perform search once first
        self.dfs_traversal(node)

        # check if any not found, if not found, mean it is in a separate subgraph (connect components)
        self.nodenames = [name for name in self.nodenames if name not in self.visited]

        # do so until no more nodes
        # loop at most N time, means each time dfs only performed once, so O(m + n)
        # otherwise, total is bounded by O(m+n) 
        while len(self.nodenames) > 0:
            self.dfs_traversal(self.nodes[self.nodenames[0]])
            self.nodenames = [name for name in self.nodenames if name not in self.visited]
    
    def dfs_traversal(self, node):
        """
        Actual Searching part for recursion
        """
        if node.name in self.visited:
            return
        self.visited.add(node.name)
        self.order.append(node.name)

        #O(m) here at most, bounded by how many connection it has.
        for child in node.children:
            self.dfs_traversal(self.nodes[child])
        

class Node:
    """
    Represent a single node in the graph
    """
    def __init__(self, name, children):
        self.name = name
        self.children = children # list of children

    def add_children(self, new_children):
        self.children.append(new_children)

    
def main():
    #begin dfs search

    # number of instances = t
    t = int(input())
    # store order for each instance
    orders = []
    for i in range(t):
        # store the number of vertices in the graph
        n = int(input())
        # list of all nodes
        nodelist = []
        for j in range(n):
            rawstr = input()
            nodelist.append(rawstr.split(' '))
        # track the first node, so began search there
        node1 = Node(nodelist[0][0], nodelist[0][1:]) if len(nodelist[0]) > 1 else Node(nodelist[0][0], [])
        nodenames = [node[0] for node in nodelist]

        # create the graph here and perform searches
        graph = Graph(nodenames)
        graph.add_node(node1)
        for i in range(1, len(nodelist)):
            if len(nodelist[i]) > 1:
                graph.add_node(Node(nodelist[i][0], nodelist[i][1:]))
            else:
                graph.add_node(Node(nodelist[i][0], []))
        
        graph.dfs(node1)
        orders.append(graph.order)
    
    # print the output, separate by spaces except last indices.
    for order in orders:
        for idx in range(len(order)):
            if idx < len(order) - 1:
                print(order[idx], end=' ')
            else:
                print(order[idx], end='')
        print()
    
if __name__ == '__main__':
    main()

