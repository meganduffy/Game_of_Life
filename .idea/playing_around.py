def make_pattern():
    pattern = ""
    pattern_string = raw_input("Enter the string you want to convert to cells: ")
    for c, x in enumerate(pattern_string):
        pattern += str(c) + "\n"
    return pattern


def points_of_string(pattern):
    pattern_lines = pattern.split("\n")
    return {(row_number, 0) for row_number, row in enumerate(pattern_lines)}


def get_cells():
    cells = points_of_string(pattern)
    board = {(c, r): (c,r) in cells for c in range(columns) for r in range(rows)}
    return board


pattern = make_pattern()
points_of_string(pattern)
get_cells()
