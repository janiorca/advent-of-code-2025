import pulp
from pathlib import Path

class Machine:
    def __init__(self, buttons, joltage):
        self.buttons = buttons
        self.joltage = joltage

path = Path.cwd() / "inputs" / "input-10.txt"
#path = Path.cwd() / "inputs" / "test_input2.txt"
lines = path.read_text().splitlines()

machines = []
for line in lines:
    parts = line.strip().split()
    buttons = [ set( [int(x) for x in btn[1:-1].split(',') ]) for btn in parts[1:-1] ]
    joltage = [ int(x) for x in parts[-1][1:-1].split( ',') ]
    machines.append( Machine( buttons, joltage))

total_button_presses = 0
for machine in machines:
    # the machine is defined as
    #
    #      [ b_00 ]        [ b_01 ]       [ b_02 ]         [ b_0K ]    [ j_0 ]
    #      [ b_10 ]        [ b_11 ]       [ b_12 ]         [ b_1K ]    [ j_1 ]
    #  p_0*[ b_20 ] +  p_1*[ b_21 ] + p_2*[ b_22 ]  +  p_K*[ b_2K ]  = [ j_2 ]
    #    ' [ ..   ]      ' [ ..   ]     ' [ ..   ]       ' [ ..   ]    [ ..  ]
    #      [ b_J0 ]        [ b_J1 ]       [ b_J2 ]         [ b_JK ]    [ j_J ]
    #..
    # wehere each column is a button and the value for the column entry is 1 if the button operates it and 0 if it doesnt
    # p_x is how many times the button is pressed  ( the solution )
    # J is length of Joltage vector
    # K is the number of buttons
    b = [ [ 1 if y in machine.buttons[x] else 0 for x in range(len(machine.buttons)) ]for y in range(len(machine.joltage)) ]
    joltages = machine.joltage.copy()
    J = len(joltages)

    # define the variables we are solving for p_0 ... p_K
    p_vars = []
    for k in range(len(b[0])):
        p = pulp.LpVariable(f"p_{k}", lowBound=0, upBound=None, cat=pulp.LpInteger  )
        p_vars.append(p)

    # Define the objective function (minimize button presses)
    prob = pulp.LpProblem("Button presses", pulp.LpMinimize)
    prob += sum(p_vars), "the total number of button presses to minimize"

    # Add the constraints
    for j in range(J):
        prob += sum( [ b[j][k]*p_vars[k] for k in range(len(b[0])) ]) == joltages[j]

    prob.solve()
    status = pulp.LpStatus[prob.status]
    print( f" Status: {status}")
    total_button_presses += prob.objective.value()

print( f"Total button presses {total_button_presses}")

