from pathlib import Path

input = Path.cwd() / "inputs/input-2.txt"
with open(input) as f:
    line = f.readline()
ranges = line.strip().split(',')

#Part1
invalid_id_sum = 0
for r in ranges:
    parts = r.split( '-')
    start = int(parts[0])
    end = int(parts[1])
    for p in range(start, end+1):
        string_no = str( p )
        str_len = len(string_no)
        if str_len&0x01:
            continue
        if string_no[:int(str_len/2)] == string_no[ int(str_len/2):]:
            invalid_id_sum += p
print( f"Part1 Invalid IDs {invalid_id_sum}")

#Part2
invalid_id_sum = 0
for r in ranges:
    parts = r.split( '-')
    start = int(parts[0])
    end = int(parts[1])
    for p in range(start, end+1):
        string_no = str( p )
        str_len = len(string_no)
        for repeat_len in range(1,int(str_len/2+1)):
            if str_len % repeat_len != 0:
                continue
            if string_no[:repeat_len] == string_no[repeat_len:repeat_len*2]:
                if all( string_no[:repeat_len] == string_no[p*repeat_len:(p+1)*repeat_len] for p in range(int(str_len/repeat_len))):
                    invalid_id_sum += p
                    break

print( f"Invalid IDs {invalid_id_sum}")
