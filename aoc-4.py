from pathlib import Path

class RollMap:
    def __init__(self, rows):
        self.rows = rows
    def width(self):
        return len(self.rows[0])
    def height(self):
        return len(self.rows)
    def get_roll_nbors(self, x, y):
        result = 0
        for dy in range(-1,2):
            for dx in range(-1,2):
                if dx == 0 and dy == 0: continue
                ix = x+dx
                iy = y+dy
                if ix < 0 or ix >= self.width(): continue
                if iy < 0 or iy >= self.height(): continue
                if self.rows[iy][ix] == '@': result += 1
        return result
    def get_accessible_rolls(self ):
        result = []
        for y in range(self.height()):
            for x in range(self.width()):
                if self.rows[y][x] != '@': continue
                if self.get_roll_nbors(x, y) < 4:
                    result.append( (y,x ))
        return result

    def remove_rolls(self, rolls):
        for y,x in rolls:
            self.rows[y][x] ='.'

input = Path.cwd() / "inputs/input-4.txt"
rows = []
with open(input) as f:
    lines = f.readlines()
    for line in lines:
        rows.append ( [ x for x in line.strip() ] )

# Part 1
roll_map = RollMap(rows)
accessible_rolls = roll_map.get_accessible_rolls()
print( f"Accessible rolls {len(accessible_rolls)}")

# Part 2
total_accessible = 0
while True:
    accessible_rolls = roll_map.get_accessible_rolls()
    total_accessible += len(accessible_rolls)
    if len(accessible_rolls) == 0:
        break
    print( f"Removing {len(accessible_rolls)} accessible rolls")
    roll_map.remove_rolls( accessible_rolls)
print(f"Total Accessible rolls {total_accessible}")
