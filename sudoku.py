from csp import CSP


class Sudoku(CSP):
    """
    Constraint Satisfation Problem Sudoku class.
    Modeling the Sudoku Game in variable, domains, neighbors and constraint method.
    """
    BLOCK_SIZE = 3
    BLOCKS_IN_ROW = 3
    ROW_SIZE = 9
    COL_SIZE = 9

    def __init__(self, grid):
        """
        Init method of Sudoku class. The parameter grid contains the definition of the sudoku board.
        This method is devoted to populate the __init_ method of CSP class, creating and passing
        variables, domains and neighbors from the grid parameter.
        """
        # Variables -
        # Variables definition. The varibles are an array with a sequence of indexes, from 0 to 80.

        self.variables = [x for x in range(self.ROW_SIZE * self.COL_SIZE)]
        # Domains -
        # Domains defintion. In this case of Sudoku CSP, the domains are '123456789' for empty cells and
        # the value of cell for cells with the default value.
        original_grid = list(grid)
        domains = {}
        for counter, item in enumerate(original_grid):
            if item == '.':
                domains[counter] = '123456789'
            else:
                restricted_domain = item
                domains[counter] = restricted_domain

        # Neighbors
        # Neighbors of binary-constraint definition. This dictionary contains the relations among a cell with its row,
        # column and block.
        neighbors = {}

        # rows
        for i in range(self.ROW_SIZE):
            row_start = i * self.BLOCKS_IN_ROW * self.BLOCK_SIZE
            row_stop = i * self.BLOCKS_IN_ROW * self.BLOCK_SIZE + self.BLOCKS_IN_ROW * self.BLOCK_SIZE
            row_indexes = list(range(row_start, row_stop))
            for item in row_indexes:
                neighbors[item] = []
                neighbors[item] += [x for x in row_indexes if x != item]

        # columns
        for b in range(self.COL_SIZE):
            col_indexes = [self.ROW_SIZE * a + b for a in range(self.COL_SIZE)]
            for item in col_indexes:
                neighbors[item] += [x for x in col_indexes if x != item]

        # blocks
        a = b = [0, 3, 6]
        for b_row in a:
            for b_col in b:
                # block
                block_items = []
                for r in range(3):
                    for c in range(3):
                        block_items.append((b_row + r) * self.ROW_SIZE + b_col + c)

                for item in block_items:
                    neighbors[item] += [x for x in block_items if x != item]

        # remove duplicates
        for item in neighbors:
            neighbors[item] = set(neighbors[int(item)])

        CSP.__init__(self, None, domains, neighbors, self.different_values_constraint)

    @staticmethod
    def different_values_constraint(A, a, B, b):
        """Constraint: neighbors has to have different value"""
        return a != b

    def display(self, assignment):
        """
        Override of CSP's method display, to present the Sudoku grid.

        :param assignment: assignment of variables
        :return: None
        """
        output = "|-----------------------------|\n|"
        for item in self.variables:
            if item in assignment:
                output += " {} ".format(assignment[item])
            else:
                output += " * "
            if not (item + 1) % 3:
                output += "|"
            if not (item + 1) % 9:
                output += "\n|"
            if not (item + 1) % 27 and item != (self.COL_SIZE * self.ROW_SIZE - 1):
                output += "-----------------------------|\n|"
        output += "-----------------------------|\n"
        print(output)
