import dataclasses
from pathlib import Path
import math
@dataclasses.dataclass
class Shape:
    rows: [[int]]

    def filled(self):
        return sum( [ x for tt in self.rows for x in tt ])

path = Path.cwd() / "inputs" / "input-12.txt"
lines = path.read_text().splitlines()

shapes = []
for idx in range(6):
    shape_rows = []
    for shape_line in range(3):
        ln_start = idx*5+shape_line + 1
        shape_ints = [ 0 if c == '.' else 1 for c in lines[ln_start] ]
        shape_rows.append(shape_ints )
    shapes.append(Shape(shape_rows))
    print(f"{idx} - {shapes[idx].filled()}")

# grids
trivial_rejections = 0
accepts = 0
for line in lines[6*5:]:
    parts = line.split()
    (x,y) = ( int(pt) for pt in parts[0][:-1].split('x'))
    available_space = x*y
    pieces = [ int(x) for x in parts[1:] ]
    min_required = sum( [ pieces[idx]*shapes[idx].filled() for idx in range(len(pieces))] )

    if min_required > available_space:
        trivial_rejections += 1
    else:
        accepts += 1

# Not my favourite problem. Discovered by accident while trying to gauge if my initial approach was correct in setting the constraint
print(f"trivial rejections {trivial_rejections}")
print(f"trivial accepts {accepts}")
print(len(shapes))

