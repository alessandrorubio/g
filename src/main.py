# Main class, or testing area
#
# Author Alessandro Rubio Moraes

from graph import Graph


def main():
	g = {
	1 : [2, 3],
	2 : [1, 4],
	3 : [1, 4],
	4 : [2, 3]
	}

	g1 = Graph(g)
	print(g1)
	print('BFS from 2')
	print(g1.bfs(2))


if __name__== '__main__':
	main()
