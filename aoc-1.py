from pathlib import Path

input = Path.cwd() / "inputs/input-1.txt"
pos = 50
at_zero_count = 0       # for part 1
with open(input) as f:
    lines = f.readlines()
    for line in lines:
        value = int( line.strip()[1:] )%100
        if line[ 0 ] == 'L':
            value = 100-value

        pos = (pos + value)%100
        if pos == 0:
            at_zero_count +=1
    print( f"at zero: {at_zero_count} times")

zero_cosses = 0
pos = 50
with open(input) as f:
    lines = f.readlines()
    for line in lines:
        original_value = int( line.strip()[1:] )
        value = original_value%100
        overflow = original_value - value
        zero_cosses += overflow / 100

        prev_pos = pos
        if line[ 0 ] == 'L':
            if value > pos:
                if pos != 0:
                    zero_cosses += 1
                pos = 100 - (value-pos)
            else:
                pos = pos - value
                if pos == 0:
                    zero_cosses += 1
        else:
            if value + pos >= 100:
                zero_cosses += 1
                pos = value + pos - 100
            else:
                pos = pos + value

print( f"{zero_cosses} zero crosses")
#6616
