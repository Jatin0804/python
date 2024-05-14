class Cell:
    def __init__(self, id: int, row: int, col: int, gold: int):
        self.id = id
        self.row = row
        self.col = col
        self.gold = gold
        self.neighbors = set()
    def __str__(self):
        return "{} - {}".format(self.id, self.gold)
    def __repr__(self):
        return "[{},{}] - {}".format(self.row, self.col, self.gold)

class Cluster:
    def __init__(self, id):
        self.id = id
        self.cells = set()
        self.total = 0
    def __repr__(self):
        return "id={}, gold={}, {}".format(self.id, self.total, self.cells)

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        index = 0
        cells = dict()

        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    index += 1
                    newCell = Cell(index, i, j, grid[i][j])
                    for c in cells.values():
                        if c.row == i and (c.col == j + 1 or c.col == j - 1) or \
                                c.col == j and (c.row == i + 1 or c.row == i - 1):
                            newCell.neighbors.add(c)
                            c.neighbors.add(newCell)
                    cells[index] = newCell

        # print(cells)
        self.clusters = dict()
        self.buildClusters(cells, index + 1)
        # print(self.clusters)
        self.result = 0
        self.path = deque()
        # for cell in cells.values():
        #     self.visit(cell, 0)

        sortedClusters = [c for c in self.clusters.values()]
        sortedClusters.sort(key=lambda cl: cl.total, reverse=True)
        # print("Sorted", sortedClusters)
        for cluster in self.clusters.values():
            self.visitCluster(cluster)

        return self.result


    def buildClusters(self, cells: dict, n: int):
        assigned = [0] * n
        for k in cells:
            cell = cells[k]
            self.tryToAddCellToCluster(cell, assigned)


    def tryToAddCellToCluster(self, cell, assigned):
        if assigned[cell.id] == 0:
            for neighbor in cell.neighbors:
                if assigned[neighbor.id] > 0:
                    cluster = self.clusters[assigned[neighbor.id]]
                    self.addCellToCluster(cluster, cell, assigned)
                    break
        if assigned[cell.id] == 0:
            index = len(self.clusters) + 1
            cluster = Cluster(index)
            self.clusters[index] = cluster
            self.addCellToCluster(cluster, cell, assigned)
        for neighbor in cell.neighbors:
            if assigned[neighbor.id] == 0:
                self.tryToAddCellToCluster(neighbor, assigned)

    def addCellToCluster(self, cluster, cell, assigned):
        cluster.cells.add(cell)
        cluster.total += cell.gold
        assigned[cell.id] = cluster.id

    def visitCluster(self, cluster: Cluster):
        if self.result >= cluster.total:
            return

        if len(cluster.cells) <= 3:
            self.result = cluster.total
            return

        self.path.clear()
        for cell in cluster.cells:
            self.visitCell(cell, 0, cluster.total)

    def visitCell(self, cell: Cell, current: int, ceiling: int):
        # print(cellId, self.path)
        self.path.append(cell.id)
        current += cell.gold
        if current > self.result:
            self.result = current
        if self.result < ceiling:
            toVisit = [c for c in cell.neighbors if c.id not in self.path]
            for neighbor in toVisit:
                self.visitCell(neighbor, current, ceiling)

        self.path.pop()