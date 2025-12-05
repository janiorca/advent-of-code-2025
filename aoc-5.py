from pathlib import Path

input = Path.cwd() / 'inputs' / 'input-5.txt'
ranges = []
ids = []
with open(input) as f:
    while True:
        line = f.readline()
        if line == '\n': break
        parts = line.split('-')
        ranges.append((int(parts[0]), int(parts[1])))
    while True:
        line = f.readline()
        if line == '': break
        ids.append( int( line ) )

# Part1
fresh_ids = 0
for id in ids:
    for range in ranges:
        if range[0] <= id <= range[1]:
            fresh_ids += 1
            break
print( f"Fresh ids{ fresh_ids} ")

#Part 2
spans = []
for range in ranges:
    while True:
        overlaps = False
        for idx, span in enumerate( spans ) :
            if not ( range[0] > span[1] or range[1] < span[0] ):
                overlaps = True
                range = ( min( span[0], range[0] ), max( span[1], range[1] ) )
                spans[ idx ] = spans[ -1]
                spans.pop()
        if overlaps == False:
            spans.append( range )
            break

total_fesh_ids = 0
for span in spans:
    total_fesh_ids += span[1] - span[0] + 1
print( f"total fresh ids {total_fesh_ids}")

