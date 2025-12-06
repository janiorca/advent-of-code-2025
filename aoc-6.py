from pathlib import Path
import math

input = Path.cwd() / "inputs" / "input-6.txt"

#Part1
rows = []
with open(input) as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        parts = line.strip().split()
        if idx < len(lines)-1:
            parts = [ int(x) for x in parts ]
        rows.append( parts )

num_parts = len(rows)-1;
total = 0;
for (idx, operation) in enumerate(rows[-1]):
    parts = [ rows[i][idx] for i in range(num_parts)]
    if operation == '+':
        total += sum( parts)
    else:
        total += math.prod( parts)
print( f"grand total {total}" )

#Part2
rows = lines
sheet_ht = len(rows)-1;
total = 0;
numbers = []
operation = rows[sheet_ht][0]
for idx in range(len(rows[0])):
    num_parts = ""
    for pt in range(sheet_ht): num_parts += rows[pt][idx]
    if num_parts.strip() == "":
        if operation == '+':
            total += sum(numbers)
        else:
            total += math.prod(numbers)
        numbers = []
        if idx < len(rows[0])-1:
            operation = rows[sheet_ht][idx+1]
    else:
        numbers.append( int(num_parts) )

print( f"grand total {total}" )