from graph import Graph


def main():
	g = {
	0 : [1, 2],
	1 : [0, 3],
	2 : [0, 3],
	3 : [1, 2]
	}

	g_direct = {
	0 : [1, 2],
	1 : [3],
	2 : [3],
	3 : []
	}

	j = {
	0 : [1, 2],
	1 : [0, 3],
	2 : [0, 3],
	3 : [1, 2],
	4 : [5],
	5 : [4]
	}

	g1 = Graph(g)
	print(g1)
	print('BFS from 2')
	print('Visited vertices: ' + str(g1.bfs(2)))
	print(''g1.bfs_path(0))
	print('- - - - - - - - - - - - -')
	
	g2 = Graph(j)
	print(g2.ucc())
	g2.reset_explored_vertices()
	print(g2.dfs_rec(0))
	g2.reset_explored_vertices()
	print(g2.dfs(0))
	g2.reset_explored_vertices()
	print('- - - - - - - - - - - - -')
	
	g1_direct = Graph(g_direct)
	print(g1_direct.topo_sort())
	g1_direct.reset_explored_vertices()



if __name__== '__main__':
	main()
