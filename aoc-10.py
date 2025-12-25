from pathlib import Path

class Machine:
    def __init__(self, lights,  buttons ):
        self.lights = lights
        self.buttons = buttons

    def find_shortest_button_sequence(self) -> int:
        # the outcome is order independent
        # the max number of combinations is 2^num_buttons
        fewest_presses = 2**len(self.buttons)
        for button_seq in range(2**len(self.buttons)):
            combo = 0
            for buttond_id in range(len(self.buttons)):
                if ( 0x00001 << buttond_id ) & button_seq:
                    combo = combo ^ self.buttons[buttond_id]
            if combo == self.lights and button_seq.bit_count() < fewest_presses:
                fewest_presses = button_seq.bit_count()
        return fewest_presses

path = Path.cwd() / "inputs" / "input-10.txt"
#path = Path.cwd() / "inputs" / "test_input2.txt"
lines = path.read_text().splitlines()

machines = []
for line in lines:
    parts = line.strip().split()
    light = [ 0 if x=='.' else 1 for x in parts[0][1:-1] ]
    lights = sum( [ val << pos for pos, val in enumerate( light ) ] )
    buttons = [ set( [int(x) for x in btn[1:-1].split(',') ]) for btn in parts[1:-1] ]
    buttons_mask = [sum([1 << val for val in btns]) for btns in buttons]
    machines.append( Machine( lights, buttons_mask))

solution_sum = 0
for machine in machines:
    solution_sum += machine.find_shortest_button_sequence()
print( f"Part 1 {solution_sum} ")
