import math

ROW_COUNT = 4 # Default is 3
COL_COUNT = 5 # Default is 4

CELL_ROW_COUNT = 10 # Default is 10
CELL_COL_COUNT = 10 # Default is 10

def primary(n, row, col):
  return math.comb(n + row + col, row + col + 1)

def secondary(n, col):
  return math.comb(n + col, col)

def get_formatted_str(j, num):
  if j == 0:
    return "{:2}".format(num)
  elif j < 3:
    return "{:3}".format(num)
  elif j < 5:
    return "{:4}".format(num)
  elif j < 8:
    return "{:5}".format(num)
  else:
    return "{:6}".format(num)

def main():
  s = ""
  for row in range(ROW_COUNT):

    for col in range(COL_COUNT):
      for j in range(CELL_COL_COUNT):
        s += "-----" 
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