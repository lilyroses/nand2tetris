# boolean_truth_table.py

# CHECK INPUT
def is_valid_input(v):
  return (type(v) == int) and (v == 0 or v == 1)



def AND(x, y):
  if is_valid_input(x) and is_valid_input(y):
    return int(x == 1 and y == 1)


def OR(x, y):
  if is_valid_input(x) and is_valid_input(y):
    return int( x == 1 or y == 1)

def NOT(x):
  if is_valid_input(x):
    if x == 0:
      return 1
    elif x == 1:
      return 0



def f(x, y, z):
  # ((x OR y) AND (NOT z))
  x_OR_y = OR(x, y)
  NOT_z = NOT(z)
  return AND(x_OR_y, NOT_z)


def incr_bin_num(bin_num):
  bin_digits = list(bin_num)

  if "0" not in digits:
    return bin_num

  if "1" not in bin_num:
    bin_digits[-1] = "1"
    incr_bin_num = "".join(bin_digits)
    return incr_bin_num
  else:

# 0     => 1 change 0 to 1
# 0 1   -> 10 change 0 to 1 and 1 to 0
# 0 0 1 --> 0 1 0 change last 0 to 1 and last 1 to 0
# 0 1 1 1 1 --> 0  change 
# 0 1 1 0 ==> 0 1 1 1 
# 1 1 0 1 --> 1 1 1 0

wwwwwwwwwwwwwwwwwwwwwwwww
xyz_combos = [
  [0, 0, 0],
  [0, 0, 1],
  [0, 1, 0],
  [0, 1, 1],
  [1, 0, 0],
  [1, 0, 1],
  [1, 1, 0],
  [1, 1, 1]
]

print("x y z | f(x, y, z)")
print("------|-------")
for x, y, z in xyz_combos:
  print(f"{x} {y} {z} |   {f(x,y,z)}")



