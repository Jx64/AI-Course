from colorama import Fore, init

class Maze:
    def __init__(self):
        self.maze = [[0, 1, 1, 1, 0],
                     [0, 1, 1, 0, 1],
                     [0, 1, 1, 1, 1],
                     [0, 1, 1, 0, 1],
                     [0, 1, 1, 1, 0]]

        self.path = []

    def nextNodeIsOne(self, x, y):
        if x < 0 or y < 0 or x >= len(self.maze) or y >= len(self.maze[0]):
            return False
        return self.maze[x][y] == 1

    def dfs(self, s, e):
        stack = [s]
        explored = [s]
        while len(stack) > 0:
            node = stack.pop()
            if node == e:
                self.path.append(node)
                return True
            row, col = node
            for direction in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if self.nextNodeIsOne(direction[0], direction[1]):
                    if direction not in explored:
                        print("node "+ str(node))
                        stack.append(direction)
                        explored.append(direction)
                        self.path.append(node)
        return False

    def print_path(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if (row, col) in self.path:
                    print(Fore.GREEN + str(self.maze[row][col]), end=" ")
                else:
                    print(Fore.RESET + str(self.maze[row][col]), end=" ")
            print()

if __name__ == "__main__":
    init(autoreset=True)
    m = Maze()

    start = (0, 1)
    end = (2, 4)
    try:
        if m.dfs(start, end):
            m.print_path()
        else:
            print("No path found")

    except ValueError:
        print("Invalid start or end point")
