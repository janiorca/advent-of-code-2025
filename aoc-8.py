from pathlib import Path

input = Path.cwd() / "inputs" / "input-8.txt"
num_connections = 1000

lines = input.read_text().splitlines()
boxes = [ [ float(c) for c in line.split(",") ] for line in lines ]

pair_distances = [ ]
for src in range(len(lines)):
    for dst in range(src+1, len(lines)):
        length = (boxes[src][0] - boxes[dst][0])**2 + (boxes[src][1] - boxes[dst][1])**2 + (boxes[src][2] - boxes[dst][2])**2
        pair_distances.append( ( length, (src, dst ) ) )
pair_distances.sort( key = lambda x: x[0])

unused_boxes = set( [tuple(box) for box in boxes ] )
box_sets = []
for idx, pair in enumerate(pair_distances):
    if idx == num_connections:
        # Part 1, solution
        circuit_sizes = sorted([len(bs) for bs in box_sets], reverse=True)
        print(f"Circuit sizes multiplied {circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]}")
        # Keep going to solve part 2

    # find the box sets that the connection boxes belong to
    set_indices = []
    for set_idx, box_set in enumerate(box_sets):
        for c in [0,1]:
            if pair[1][c] in box_set:
                set_indices.append( set_idx )
    set_indices = list(set(set_indices))

    match len( set_indices ):
        case 0:
            # the pair boxes did not fit any box sets, create a new set
            box_sets.append( set( pair[1]) )
            unused_boxes.discard( tuple( boxes[ pair[1][0] ] ) )
            unused_boxes.discard( tuple( boxes[ pair[1][1] ] ) )
        case 1:
            # The box pair only belongs to one set. Expand the set
            box_sets[ set_indices[0] ] = box_sets[ set_indices[0] ].union( pair[1])
            unused_boxes.discard( tuple( boxes[ pair[1][0] ] ) )
            unused_boxes.discard( tuple( boxes[ pair[1][1] ] ) )
        case 2:
            #the box pair joins two sets. Merge them
            box_sets[ set_indices[0] ] = box_sets[ set_indices[0] ].union( box_sets[ set_indices[1] ])
            box_sets[ set_indices[1] ] = box_sets[ set_indices[0] ]
            box_sets[set_indices[1]]  = box_sets[ -1]
            box_sets.pop()

    if len( box_sets ) == 1 and len( unused_boxes ) ==0 :
        X1 = boxes[pair[1][0]][0]
        X2 = boxes[pair[1][1]][0]
        print(f"Part2. Last connection mul sum {X1*X2}")
        break