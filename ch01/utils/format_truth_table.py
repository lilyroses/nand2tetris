def format_truth_table(inputs, outputs, func_name):

  """
+-----------+--------------+
| x   y   z |  AND(x,y,z)  |
+-----------+--------------+
| 0   0   0 |       0      |
| 0   0   1 |       1      |
| 0   1   0 |       1      |
| 0   1   1 |       1      |
| 1   0   0 |       1      |
| 1   0   1 |       1      |
| 1   1   0 |       1      |
| 1   1   1 |       1      |
+-----------+--------------+

  """
  table = ""

  vars = list("xyz")[:len(inputs[0])]

  input_args_fmt = '  '.join(vars)
  input_args_fmt = f" {input_args_fmt} "

  func_args_fmt = ','.join(vars)
  func_name_fmt = f"  {func_name}({func_args_fmt})  "

  border_section_1 = "-" * len(input_args_fmt)
  border_section_2 = "-" * len(func_name_fmt)
  border = f"+{border_section_1}+{border_section_2}+\n"

  col_headers = f"|{input_args_fmt}|{func_name_fmt}|\n"

  table += border
  table += col_headers
  table += border

  for i in range(len(inputs)):
    bits_fmt = '  '.join([str(b) for b in inputs[i]])
    bits_fmt = f" {bits_fmt} "

    n = len(func_name_fmt)
    output_fmt = str(outputs[i]).center(n)

    row = f"|{bits_fmt}|{output_fmt}|\n"
    table += row

  table += border

  return table


if __name__ == "__main__":

  inputs = [[0,0], [0,1], [1,0], [1,1]]
  fn = "AND"
  outputs = [0,0,0,1]
  print(format_truth_table(inputs, outputs, fn))

  fn = "OR"
  outputs = [0,1,1,1]
  print(format_truth_table(inputs, outputs, fn))



  inputs = [[0],[1]]
  fn = "NOT"
  outputs = [1,0]
  print(format_truth_table(inputs, outputs, fn))



  inputs = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],
            [1,0,0],[1,0,1],[1,1,0],[1,1,1]]

  fn = "AND"
  outputs = [0,0,0,0,0,0,0,1]
  print(format_truth_table(inputs, outputs, fn))


  fn = "OR"
  outputs = [0,1,1,1,1,1,1,1]
  print(format_truth_table(inputs, outputs, fn))


  fn = "NAND"
  outputs = [1,1,1,1,1,1,1,0]
  print(format_truth_table(inputs, outputs, fn))

