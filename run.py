import argparse
import tracemalloc
import time
import os
from sudoku import Sudoku

from solutions import arc_cons, forward_checking, no_inference, lcv, mrv, first_unassigned_variable, unordered_domain_values, \
    backtracking_search

dir_path = os.path.dirname(os.path.realpath(__file__))

start = time.time()
tracemalloc.start()
def board_file(path):
    with open(path) as f:
        board = f.readline()
    return board


arg_to_function = {
    # Inference
    'no_inference': no_inference,
    'arc_cons': arc_cons,
    'forward_checking': forward_checking,
    # Value ordering
    'unordered_domain_values': unordered_domain_values,
    'lcv': lcv,
    # Variable ordering
    'first_unassigned_variable': first_unassigned_variable,
    'mrv': mrv,
}

# parse args
parser = argparse.ArgumentParser(description='sudoku')
parser.add_argument('-b', '--board', help='board')
parser.add_argument('-valo', '--valordering', help='value ordering')
parser.add_argument('-varo', '--varordering', help='variable ordering')
parser.add_argument('-inf', '--inference', help='inference')
args = parser.parse_args()

# default values
board = board_file(os.path.join(dir_path, 'boards/example.txt'))
valordering = unordered_domain_values
varordering = first_unassigned_variable
inference = no_inference

# replace defaults
if args.board:
    board = board_file(os.path.join(dir_path, 'boards/{}.txt'.format(args.board)))
if args.valordering:
    valordering = arg_to_function[args.valordering]
if args.varordering:
    varordering = arg_to_function[args.varordering]
if args.inference:
    inference = arg_to_function[args.inference]

s = Sudoku(board)
s.display(s.infer_assignment())
backtracking_search(s, varordering, valordering, inference)
s.display(s.infer_assignment())
sum = 0
for n in range(1,500):
    sum += n
print("Run Time: " + str( time.time() - start ))
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
tracemalloc.stop()