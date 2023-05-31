class Node:
    def __init__(self, data, level, fval):
        #Initialize the node with the data, level of the node, and the calculated f-value
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        #Generate child nodes from the given node by moving the blank space either in the four directions {up, down, left, right}
        x, y = self.find_blank(self.data)
        val_list = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []
        for i in val_list:
            child = self.move_blank(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level+1, 0)
                children.append(child_node)
        return children

    def move_blank(self, puz, x1, y1, x2, y2):
        # Move the blank space in the given direction and if the position values are out of bounds, return None
        if 0 <= x2 < len(puz) and 0 <= y2 < len(puz):
            temp_puz = self.copy_puzzle(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy_puzzle(self, puzzle):
        # Create a copy of the given puzzle matrix
        temp = []
        for i in puzzle:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find_blank(self, puzzle):
       # Find the position of the blank space in the puzzle
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if puzzle[i][j] == '_':
                    return i, j


class PuzzleSolver:
    def __init__(self, size):
        """ Initialize the puzzle solver with the specified puzzle size, open and closed lists as empty """
        self.size = size
        self.open = []
        self.closed = []

    def accept_puzzle(self):
        """ Accept the start and goal state of the puzzle from the user """
        start_state = []
        goal_state = []
        print("Enter the start state of the puzzle:")
        for _ in range(self.size):
            row = input().split()
            start_state.append(row)
        print("Enter the goal state of the puzzle:")
        for _ in range(self.size):
            row = input().split()
            goal_state.append(row)
        return start_state, goal_state

    def heuristic(self, start, goal):
        """ Heuristic function to calculate the heuristic value h(x) """
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    count += 1
        return count

    def a_star(self):
        """ Perform the A* algorithm to solve the puzzle """
        start_state, goal_state = self.accept_puzzle()
        start_node = Node(start_state, 0, 0)
        start_node.fval = self.heuristic(start_state, goal_state)
        self.open.append(start_node)

        while True:
            current_node = self.open[0]

            if self.heuristic(current_node.data, goal_state) == 0:
                break

            for child_node in current_node.generate_child():
                child_node.fval = self.heuristic(child_node.data, goal_state)
                self.open.append(child_node)

            self.closed.append(current_node)
            del self.open[0]
            self.open.sort(key=lambda x: x.fval, reverse=False)

    def print_solution(self):
        """ Print the steps of the solution """
        print("Solution Steps:")
        for node in self.closed:
            for row in node.data:
                print(*row)
            print()
            print("  | ")
            print(" \\/")
            print()

        goal_node = self.closed[-1]
        print("Goal State Reached:")
        for row in goal_node.data:
            print(*row)


puzzle_solver = PuzzleSolver(3)
puzzle_solver.a_star()
puzzle_solver.print_solution()
