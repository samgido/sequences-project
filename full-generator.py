import math

# rows/cols of cells 
ROW_COUNT = 3 # Default is 3
COL_COUNT = 4 # Default is 4

# rows/cols in each cell
CELL_ROW_COUNT = 10 # Default is 10
CELL_COL_COUNT = 10 # Default is 10

# used for formatting
MAX_NUM_LENGTHS = [0 for _ in range(CELL_COL_COUNT)]

# P(n), dependent on row and column of current cell
def primary(n, row, col):
  return math.comb(n + row + col, row + col + 1)

# S(n), only dependent on the column of the current cell
def secondary(n, col):
  return math.comb(n + col, col)

# finds the max 'width' of each column in a cell, uses this as formatting for all cells
def initialize_formatting():
  i =  CELL_ROW_COUNT - 1
  col = COL_COUNT - 1
  row = ROW_COUNT - 1

  for j in range(CELL_COL_COUNT):
    num = secondary(j, col) + primary(j, row, col) * i
    MAX_NUM_LENGTHS[j] = len(str(num))

def get_formatted_str(j, num):
  form = "{:" + str(MAX_NUM_LENGTHS[j] + 1) + "}"
  return form.format(num)

def main():
  initialize_formatting() 

  s = ""
  for row in range(ROW_COUNT):

    # printing borders
    for col in range(COL_COUNT):
      for j in range(sum(MAX_NUM_LENGTHS) + len(MAX_NUM_LENGTHS)):
        s += "-" 
      s += "--" 
    s += "\n"

    # printing P(n) at the top of each cell
    for col in range(COL_COUNT):
      for j in range(CELL_COL_COUNT):
        num = primary(j, row, col)
        s += get_formatted_str(j, num)

      s += " |"
    s += "\n"

    # printing the rest of the cell
    for i in range(CELL_ROW_COUNT - 1): 
      for col in range(COL_COUNT):
        for j in range(CELL_COL_COUNT):
          num = secondary(j, col) + primary(j, row, col) * i
          s += get_formatted_str(j, num)

        s += " |"
      s += "\n"
  
  # writing to output.txt
  with open("output.txt", "w") as file:
    file.write(s)

main()