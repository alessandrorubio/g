# Main class, or testing area
#
# Author Alessandro Rubio Moraes

from graph import Graph


def main():
	g = Graph(
      [0, 1, 2, 3, 4, 5, 6], 
      [[1, 3], [0, 2], [1], [0, 4], [3], [6], [5]]
      )

	print(g)
	print(g.bfs(2))
	print(g.bfs_path(1))
	print(g.ucc())
	print(g.dfs(0))


if __name__== '__main__':
	main()
