import numpy
import math

ROW_COUNT = 3 # Default is 3
COL_COUNT = 4 # Default is 4

CELL_ROW_COUNT = 10 # Default is 10
CELL_COL_COUNT = 10 # Default is 10

MAX_NUM_LENGTHS = [0 for _ in range(CELL_COL_COUNT)]

def primary(n, row, col):
  return math.comb(n + row + col, row + col + 1)

def secondary(n, col):
  return math.comb(n + col, col)

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

    for col in range(COL_COUNT):
      for j in range(sum(MAX_NUM_LENGTHS) + len(MAX_NUM_LENGTHS)):
        s += "-" 
      s += "--" 
    s += "\n"

    for col in range(COL_COUNT):
      for j in range(CELL_COL_COUNT):
        num = primary(j, row, col)
        s += get_formatted_str(j, num)

      s += " |"
    s += "\n"

    for i in range(CELL_ROW_COUNT - 1): 
      for col in range(COL_COUNT):
        for j in range(CELL_COL_COUNT):
          num = secondary(j, col) + primary(j, row, col) * i
          s += get_formatted_str(j, num)

        s += " |"
      s += "\n"
  
  with open("output.txt", "w") as file:
    file.write(s)

main()