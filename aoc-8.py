from pathlib import Path

input = Path.cwd() / "inputs" / "input-8.txt"
#input = Path.cwd() / "inputs" / "test_input.txt"
num_connections = 1000

lines = input.read_text().splitlines()
boxes = [ [ float(c) for c in line.split(",") ] for line in lines ]

pair_distances = [ ]
for src in range(len(lines)):
    for dst in range(src+1, len(lines)):
        length = (boxes[src][0] - boxes[dst][0])**2 + (boxes[src][1] - boxes[dst][1])**2 + (boxes[src][2] - boxes[dst][2])**2
        pair_distances.append( ( length, (src, dst ) ) )
pair_distances.sort( key = lambda x: x[0])
pair_distances = pair_distances[ :num_connections]

box_sets = []
for pair in pair_distances:
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
        case 1:
            # The box pair only belongs to one set. Expand the set
            box_sets[ set_indices[0] ] = box_sets[ set_indices[0] ].union( pair[1])
        case 2:
            #the box pair joins two sets. Merge them
            box_sets[ set_indices[0] ] = box_sets[ set_indices[0] ].union( box_sets[ set_indices[1] ])
            box_sets[ set_indices[1] ] = box_sets[ set_indices[0] ]
            box_sets[set_indices[1]]  = box_sets[ -1]
            box_sets.pop()

circuit_sizes = sorted([ len(bs) for bs in box_sets ], reverse=True)
print( f"Circuit sizes multiplied {circuit_sizes[0]*circuit_sizes[1]*circuit_sizes[2]}")