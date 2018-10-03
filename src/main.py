# Main class, or testing area
#
# Author Alessandro Rubio Moraes

from graph import Graph


def main():
    g = Graph([1, 2, 3, 4], [[2], [3], [4], [2]])
    print(g)


if __name__== '__main__':
	main()
