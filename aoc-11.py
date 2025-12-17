import dataclasses
import functools
from pathlib import Path

@dataclasses.dataclass
class Node:
    name: str
    dests: set()

@functools.cache
def calc_paths( path_src: str, path_dest: str ) -> int:
    if path_src == path_dest: return 1
    if path_src in global_nodes:
        curr_node = global_nodes[ path_src ]
        num_paths = 0
        for dest in curr_node.dests:
            num_paths += calc_paths( dest, path_dest )
        return num_paths
    else:
        return 0

def get_nodes( lines: [] ) -> {}:
    nodes = {}
    for line in lines:
        parts = line.split(' ')
        nodes[parts[0][:-1]] = Node(parts[0][:-1], set(parts[1:]))
    return nodes

path = Path.cwd() / "inputs" / "input-11.txt"
lines = path.read_text().splitlines()

#Part 1
global_nodes = get_nodes( lines )
you_out = calc_paths( "you", "out" )
print( f" paths from you to out {you_out}  ")

#Part 2
svr_fft = calc_paths( "svr", "fft")
fft_dac = calc_paths( "fft", "dac")
dac_out = calc_paths( "dac", "out")
print( f"total paths via fft and dac {svr_fft*fft_dac*dac_out}")