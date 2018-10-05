# Main class, or testing area
#
# Author Alessandro Rubio Moraes

from graph import Graph


def main():
	g = Graph(
      [0, 1, 2, 3, 4, 5, 6], 
      [[1, 3], [0, 2], [1], [0, 4], [3, 5], [4, 6], [5]]
      )

	g2 = Graph(
		[0, 1, 2, 3],

		[[1, 2], [], [3], []]
		)

	g3 = Graph(
		[0, 1, 2, 3, 4],
		[[1, 3], [4], [0, 3], [1, 3], []])

	print(g2)
	print(g2.topoSort())
	print("- - - - - - - - -")
	print(g3)
	print(g3.topoSort())


if __name__== '__main__':
	main()
