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
            ans += "\t" + str(self.v[i]) + ": " + str(self.e[i]) + "\n"
        return ans

    def bfs(self, s):
      """
      Vanilla version of the BFS algorithm, each iteration 
      explores a new vertex that is connected to s.
      M corresponds to the adjacency list of visited vertices.
      Q is a Queue.
      s is the starting point vertex.
      It returns the M.
      """
      M = [0 for v in self.v]
      M[s] = 1
      Q = [s]
      while Q:
        w = Q[0]
        Q.remove(w)
        for i in self.e[w]:
          if M[i] == 0:
            M[i] = 1
            Q.append(i)
      return M
    
    def bfs_path(self, s):
      """
      Path version of the BFS algorithm. This version returns an array P which
      every vertex corresponds to the distance between s and v.
      Q is a Queue type data structure.
      M corresponds to the adjacency list of visited vertices.
      """
      M = [0 for v in self.v]
      P = [0 for v in self.v]
      M[s] = 1
      P[s] = 0
      Q = [s]
      while Q:
        w = Q[0]
        Q.remove(w)
        for i in self.e[w]:
          if M[i] == 0:
            M[i] = 1
            P[i] = P[w] + 1
            Q.append(i)
      return P
    
    # CS
    def ucc(self):
      """
      UCC stands for Undirected Connected Components. ucc() returns an
      array CC where each index corresponds to a connected component.
      Q is a Queue type data structure.
      M corresponds to the adjacency list of visited vertices.
      """
      M = [0 for v in self.v]
      CC = [0 for v in self.v]
      numCC = 0
      for i in self.v:
        if M[i] == 0:
          numCC += 1
          Q = [i]
          while Q:
            w = Q[0]
            Q.remove(w)
            CC[w] = numCC
            for edge in self.e[w]:
              if M[edge] == 0:
                M[edge] = 1
                Q.append(edge)
      return CC
    

    def dfs(self, s):
      """
      Vanilla version of the DFS algorithm. dfs() returns an array M
      which corresponds to the adjancecy list of visited/explored vertices.
      The difference between dfs() and bfs() is the way it explores the graph 
      and the data structure usedto iterate between the vertices.
      S is a stack data structure. Using append() and pop() to simulate it.
      """
      M = [0 for v in self.v]
      S = [s]
      while S:
        v = S.pop()
        if M[v] == 0:
            M[v] = 1
            for i in self.e[v]:
                S.append(i)
      return M

    def topoSort(self):
        """
        Topological sorting using DFS algorithm. It returns
        a list P which every index corresponds to the order of the
        topological sort (from 1 to n).
        """
        M = [0 for v in self.v]
        P = [0 for v in self.v]
        S = []
        Q = []
        current = len(self.v)

        for vertex in self.v:
            if M[vertex] == 0:
                S.append(vertex)
                while S:
                    v = S.pop()
                    if M[v] == 0:
                        M[v] = 1
                        for w in self.e[v]:
                            S.append(w)
                        P[v] = current
                        current -= 1
        return P[::-1]