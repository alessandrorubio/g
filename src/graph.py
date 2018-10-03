# Simple graph class to help me understand
# graphs algorithms and some data structures.
# 
# Author: Alessandro Rubio Moraes


class Graph:
    def __init__(self, v, e):
        """
        Initializer of Graph. We suppose v is a list
        of vertices and e the adjacency list.
        """
        self.v = v
        self.e = e

    def __repr__(self):
        """
        Representation of Graph. It prints vertices and edges in
        dictionnary way.
        """
        ans = 'Vertices :\n'
        for i in range(len(self.v)):
            ans += str(self.v[i]) + ": " + str(self.e[i]) + "\n"
        return ans


