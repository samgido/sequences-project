import math

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
  for row in range(3):

    for col in range(4):
      for j in range(10):
        num = primary(j, row, col)
        s += get_formatted_str(j, num)

      s += " |"
    s += "\n"

    for i in range(9):
      for col in range(4):
        for j in range(10):
          num = secondary(j, col) + primary(j, row, col) * i
          s += get_formatted_str(j, num)

        s += " |"
      s += "\n"
    
    s += "\n"
  
  with open("output.txt", "w") as file:
    file.write(s)

main()