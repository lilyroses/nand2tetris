# increment_binary_number.py

def increment_binary_number(binary_number):
  binary_digits = [int(d) for d in str(binary_number)]
  n = len(binary_digits)

  # if binary num is all ones, change all bits to 0 and prepend a 1
  if 0 not in binary_digits:
    binary_digits = [0 for i in range(n)]
    binary_digits.insert(1,0)
  else:
    if binary_digits[-1] == 0:
      binary_digits[-1] = 1
    else:
      # the index of the last 0 in the binary number is the
      # the digit place that will be fl.]'ipped over
      i = binary_digits.rfind(0)

binary_digits[i] = 1
    
  return "".join(binary_digits)


# find last 0
# if none, change all but the first digit to 0s, then append a 1
# if not in digits, bin_digits = [1] +  [0 for i in range(len(k
# 1011011 -> 1011100 (find last consec. string of 1s, (or last 0), change preceding 0 to 1, change 1s to 0s)
# 1011100 -> 1011101 (
# 1111111 -> 10000000
# 1010111 - > 1011000
# 111 -> 1000
# 10010110001 -> 10010110010
00000000
00000001  - ends in 1: find closest 0 and switch to 1,
00000010
00000011
00000100
00000101
00000110
00000111
00001000
00001001
00001010
00001011
00001100
00001101
00001110
00001111
00010000
00010001
00010010
00010011
00010100
00010101
00010110
00010111
00011000
00011001
00011010
00011011
00011100
00011101

11111111

