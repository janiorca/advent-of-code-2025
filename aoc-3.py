from pathlib import Path

input = Path.cwd() / "inputs/input-3.txt"
with open(input) as f:
    lines = f.readlines()

#Part1
joltage = 0
for line in lines:
    line = line.strip()
    left_digit = max( [ x for x in line[:-1] ])
    digit_pos = line.find( left_digit )
    right_digit = max( [ x for x in line[digit_pos+1:] ])
    jolt = int( left_digit + right_digit )
    joltage += jolt
print( f"Total joltage {joltage}")

#Part2
joltage = 0
for line in lines:
    number = ""
    line = line.strip()
    available_digit = 0
    for digit_no in range( 12 ):
        line_len = len( line )
        digit = max( [ x for x in line[available_digit:(line_len-(11-digit_no))] ])
        number += digit
        available_digit = line.find( digit, available_digit )+1

    jolt = int( number )
    joltage += jolt
print( f"Total joltage {joltage}")
