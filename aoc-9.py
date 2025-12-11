import bisect
from pathlib import Path
from collections import defaultdict

path = Path.cwd() / "inputs" / "input-9.txt"
lines = path.read_text().splitlines()
points = [ [ int(c) for c in line.split(',')] for line in lines ]

# Part 1
all_squares = []
for outer in points:
    for inner in points:
        min_y, max_y = min(outer[1], inner[1]), max(outer[1], inner[1])
        min_x, max_x = min(outer[0], inner[0]), max(outer[0], inner[0])
        area = (max_x - min_x+1) * (max_y - min_y+1)
        all_squares.append( ( area, (min_x, min_y, max_x, max_y) ))

all_squares.sort( key=lambda x:x[0], reverse=True)
print( f"largest square {all_squares[0][0]}" )

#Part2
# Build the span table to make it faster to asnwer questions about the points being inside the shape
num_points = len(points)
span_dict = defaultdict( lambda : [ set(), set() ])           # separate list for starts and end spans
for ln in range( num_points ):
    y1 = points[ln][1]
    x1 = points[ln][0]
    y2 = points[(ln+1)%num_points][1]
    x2 = points[(ln+1)%num_points][0]
    if y1 == y2:
        # horizontal line
        span_dict[y1][0].add( min( x1, x2) )
        span_dict[y1][1].add( max( x1, x2) )
    elif y2 > y1:
        # vertical down (record span stops)
        for y in range( y1, y2+1 ):
            span_dict[y][1].add( x1 )
    else:
        # vertical down (record span starts)
        for y in range( y2, y1+1 ):
            span_dict[y][0].add( x1 )

# sort the spans
for key in span_dict.keys():
    span_dict[key][0] = sorted( span_dict[key][0] )
    span_dict[key][1] = sorted( span_dict[key][1] )

def is_point_valid( x, y, span_dict ) :
    # if the points is not valid return false,
    # if it is valid, return the highets x - coordinate that is inside the spn to accelerate the horizontal evaluation
    span_idx = bisect.bisect_right( span_dict[y][0], x )
    if span_idx == 0: return None
    span_stop_x = span_dict[y][1][span_idx-1]
    if span_stop_x < x: return None
    return span_stop_x

largest_square = 0
total = len(all_squares)
progress = 0
# earch to the squares in size order, starting with the largest
for area, (min_x, min_y, max_x, max_y) in all_squares:
    if progress % 1000 == 0:
       print( f"{progress} / {total}")
    progress += 1
    # Are all the square points inside the shaped defined by the spans
    # We only need to check that the outline of the box is inside the shape If any part of the box is not inside the
    # shape the outline must also be broken
    is_valid = True
    x = min_x
    while x < max_x:
        nx = is_point_valid(x, min_y, span_dict)
        if  nx == None:
            is_valid = False
            break
        x = nx+1
    if is_valid == True:
        x = min_x
        while x < max_x:
            nx = is_point_valid(x, min_y, span_dict)
            if nx == None:
                is_valid = False
                break
            x = nx + 1
    if is_valid == True:
        for y in range(min_y, max_y + 1):
            if not is_point_valid(min_x, y, span_dict) or not is_point_valid(max_x, y, span_dict):
                is_valid = False
                break
    if is_valid:
        largest_square = area
        break

print( f"largest square {largest_square}" )