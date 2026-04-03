'''
you are given a 2D grid where each cell is one of:

    '.' - empty space (you can walk here)

    '#' - wall (you cannot walk here)

    '@' - starting position

    'E' - exit 

You can move up, down, left, right (no diagonals), and you cannot move outside the grid. 

can_reach_exit([
    "@..",
    ".#E",
    "..."
])
output = True
# One path: (0,0)->(0,1)->(0,2)->(1,2) which is 'E'

can_reach_exit([
    "@#E"
])
output = False
# Exit is blocked by a wall

can_reach_exit([
    "@.#.",
    "..#E",
    "####"
])
output = False

can_reach_exit([
    "@...",
    ".###",
    "...E"
])
output = True
'''


def get_valid_neighbors(pos,map):
    # y-1
    current_pos=pos
    ...


def can_reach_exit(map):
    current_pos = 0,0
    neighbors = get_valid_neighbors(current_pos,map)
    
    
    ...




    
can_reach_exit([
    "@..",
    ".#E",
    "..."
])
    
# assert can_reach_exit([
#     "@..",
#     ".#E",
#     "..."
# ]) == True
# # One path: (0,0)->(0,1)->(0,2)->(1,2) which is 'E'

# assert can_reach_exit([
#     "@#E"
# ]) == False
# # Exit is blocked by a wall

# assert can_reach_exit([
#     "@.#.",
#     "..#E",
#     "####"
# ]) == False

# assert can_reach_exit([
#     "@...",
#     ".###",
#     "...E"
# ]) == True



"""
hint -> depth-first search

step 1: find neighbors!
    - weird note: y comes first here because of how lists work (y, x)

    (y, x) -> y - 1, y + 1, x - 1, x + 1

step 2: validate neighbors!
    - positions cannot be negative
    - positions cannot be greater than the length of the columns/rows


    (0, 0), -> (0, 1), -> (0, 2)
       |          |         |
       v          v         v
    (1, 0), -> (1, 1), -> (1, 2)
       |          |         |
       v          v         v
    (2, 0), -> (2, 1), -> (2, 2)

"""