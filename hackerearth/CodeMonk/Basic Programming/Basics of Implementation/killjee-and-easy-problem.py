""" UNSOLVED """

def calculate_path(edges):
    path = []
    path.append(edges[0][0])
    for edge in edges:
        if edge[0] == path[len(path)-1]:
            path.append(edge[1])
    print(len(path))
    print(path)


def main():
    noOfNodes, noOfEdges = list(map(int, input().strip().split(' ')))
    edges = []
    for iterator in range(noOfEdges):
        edges.append(list(map(int, input().strip().split(' '))))
    calculate_path(edges)


if __name__ == '__main__':
    main()
