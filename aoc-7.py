import copy
from pathlib import Path

input = Path.cwd() / "inputs" / "input-7.txt"
#input = Path.cwd() / "inputs" / "test_input.txt"

lines = input.read_text().splitlines()
lines = [ ['.'] + [ ch for ch in line ] + ['.']for line in lines ]
# Find the start
pos  = next( (i for i, x in enumerate(lines[0] ) if x == 'S' ), None )
lines[0][pos] = '|'
# Paint the paths
for line_idx in range(1,len(lines)):
    new_line = ['.']
    for column_idx in range(1,len(lines[0])-1):
        if lines[line_idx][column_idx] == '^': new_line.append('^')
        elif lines[line_idx-1][column_idx] == '|' or lines[line_idx][column_idx-1] == '^' or lines[line_idx][column_idx+1] == '^':
            new_line.append( '|' )
        else:
            new_line.append( '.' )
    lines[ line_idx ] = new_line + ['.']

#Part1
split_count = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '^' and lines[y-1][x] == '|':
            split_count += 1
print(f"split count {split_count}")

# Part2
counts = [[0 for x in range( len(lines[0]))] for y in  range(len(lines) )]
counts[0][pos] = 1
new_counts = copy.deepcopy(counts)
for line_idx in range(1,len(lines)):
    for column_idx in range(1, len(lines[0])-1):
        if lines[line_idx][column_idx] == '^': continue
        if lines[line_idx-1][column_idx] == '|':
            new_counts[line_idx][column_idx] += counts[line_idx-1][column_idx]
        if lines[line_idx][column_idx+1] == '^':
            new_counts[line_idx][column_idx] += counts[line_idx-1][column_idx+1]
        if lines[line_idx][column_idx-1] == '^':
            new_counts[line_idx][column_idx] += counts[line_idx-1][column_idx-1]
    counts = copy.deepcopy(new_counts)

print( f"Many world splits {sum(counts[len(lines)-1])}")
