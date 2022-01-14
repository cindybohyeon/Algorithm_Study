import sys
si = sys.stdin.readline

N, M = map(int, si().split())
edges = [list(map(int, si().split())) for _ in range(M)]


class Graph(object):
    def __init__(self, N):
        self.N = N
    
    def add_edge(self, x, y, bidirect=True):
        pass

    def is_x_y_con(self, x, y):
        pass

    def get_con_by_x(self, x):
        pass


class Matrix(Graph):
    def __init__(self, N):
        super().__init__(N)
        self.con = [[0 for _ in range(N + 1)] for __ in range(N + 1)]

    def add_edge(self, x, y, bidirect=True):
        self.con[x][y] = 1
        if bidirect:
            self.con[y][x] = 1

    def is_x_y_con(self, x, y):
        return self.con[x][y] == 1

    def get_con_by_x(self, x):
        return [y
                for y in range(N + 1)
                if self.con[x][y] == 1
                ]

class List(Graph):
    def __init__(self, N):
        super().__init__(N)
        self.con = [[] for _ in range(N + 1)]

    def add_edge(self, x, y, bidirect=True):
        self.con[x].append(y)
        if bidirect:
            self.con[y].append(x)

    def is_x_y_con(self, x, y):
        return y in self.con[x]

    def get_con_by_x(self, x):
        return self.con[x]

matrix = Matrix(N)
list = List(N)
for edge in edges:
    matrix.add_edge(edge[0], edge[1])
    list.add_edge(edge[0], edge[1])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        assert matrix.is_x_y_con(i, j) == list.is_x_y_con(i, j)


for i in range(1, N + 1):
    assert matrix.get_con_by_x(i) == sorted(list.get_con_by_x(i))

visited = [False for _ in range(N + 1)]
def dfs(vertex: int, graph: Graph):
    '''
    :return: graph에서 vertex에서 갈 수 있는 모든 정점을 다 확인한다.
    '''
    visited[vertex] = True
    for adj in graph.get_con_by_x(vertex):
        if not visited[adj]:
            # adj에서 다시 갈 수 있는 모든 정점을 확인하고 싶어
            dfs(adj, graph)

# dfs(1, matrix)
dfs(1, list)
print(sum([1 for x in range(N + 1) if visited[x]]) - 1)