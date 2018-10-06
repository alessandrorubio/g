# Simple graph class to help me understand
# graphs algorithms and some data structures.
# 
# Author: Alessandro Rubio Moraes


class Graph:
    def __init__(self, v):
        """
        Initializer of Graph. We suppose v is a dictionnary where
        keys are the vertices and the values are the edges. We store
        the visited edges in a set.
        """
        self.v = v
        self.explored_vertices = set()
        self.current = len(v)
        self.top_order = [0 for x in v]

    def __repr__(self):
        """
        Representation of Graph. It prints vertices and edges in
        dictionnary way.
        """
        ans = ''
        for vertex, edge in self.v.items():
          ans += str(vertex) + ' -> ' + str(edge) +'\n'
        return ans

    def reset_explored_vertices(self):
      """
      Resets explored_vertices' set.
      """
      self.explored_vertices = set()

    def reset_current(self):
      """
      Resets current to cardinal of v
      """
      self.current= len(self.v)

    def bfs(self, s):
      """
      BFS algorithm, each iteration explores a new vertex that is connected to s.
      s is the starting point vertex.
      Returns the set of explored vertices.
      """
      self.explored_vertices.add(s)
      Q = [s]
      while Q:
        w = Q[0]
        Q.remove(w)
        for i in self.v[w]:
          if i not in self.explored_vertices:
            self.explored_vertices.add(i)
            Q.append(i)
      return self.explored_vertices
    
    def bfs_path(self, s):
      """
      Path version of the BFS algorithm.
      Returns a list P which every index corresponds
      to the distance between itself and s.
      """
      self.reset_explored_vertices()
      self.explored_vertices.add(s)
      P = [0 for v in self.v]
      P[s] = 0
      Q = [s]
      while Q:
        w = Q[0]
        Q.remove(w)
        for i in self.v[w]:
          if i not in self.explored_vertices:
            self.explored_vertices.add(i)
            P[i] = P[w] + 1
            Q.append(i)
      return P
    
    # CS
    def ucc(self):
      """
      UCC stands for Undirected Connected Components.
      Q is a Queue type data structure.
      Returns a list CC where each index corresponds to a connected component.
      """
      self.reset_explored_vertices()
      CC = [0 for v in self.v]
      numCC = 0
      for i in self.v:
        if i not in self.explored_vertices:
          numCC += 1
          Q = [i]
          while Q:
            w = Q[0]
            Q.remove(w)
            CC[w] = numCC
            for edge in self.v[w]:
              if edge not in self.explored_vertices:
                self.explored_vertices.add(edge)
                Q.append(edge)
      return CC
    

    def dfs(self, s):
      """
      Iterative version of the DFS algorithm. 
      S is a stack data structure; Using append() and pop() to simulate it.
      Returns a set containing every explored vertex.
      """
      self.reset_explored_vertices()
      S = [s]
      while S:
        v = S.pop()
        if v not in self.explored_vertices:
            self.explored_vertices.add(v)
            for w in self.v[v]:
                S.append(w)
      return self.explored_vertices

    def dfs_rec(self, s):
      """
      Recursive version of the DFS algorithm. Returns a set
      containing all the explored vertices.
      """
      self.explored_vertices.add(s)
      for edge in self.v[s]:
        if edge not in self.explored_vertices:
          self.dfs_rec(edge)
      return self.explored_vertices

    def dfs_topo(self, s):
      """
      DFS subroutine to be used in topo_sort() only.
      """
      self.explored_vertices.add(s)
      for v in self.v[s]:
        if v not in self.explored_vertices:
          self.dfs_topo(v)
      self.top_order[s] = self.current
      self.current -= 1

    def topo_sort(self):
      """
      Returns a topological sorting of the graph.
      """
      self.reset_explored_vertices()
      self.reset_current()

      for v in self.v:
        if v not in self.explored_vertices:
          self.dfs_topo(v)
      return self.top_order