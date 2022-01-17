with open ("day24.txt", "r") as f:
    instr = [i.split(" ") for i in f.read().split("\n")]

inp_str = "13579246899999"

def run_program (inp_str):
    registers = {"w": 0, "x": 0, "y": 0, "z": 0}
    for ins in instr:
        if ins[0] == "inp":
            registers[ins[1]] = int(inp_str[0])
            inp_str = inp_str[1:]
        else:
            lval, rval = ins[1], ins[2]
            if rval in registers:
                rval = registers[rval]
            else:
                rval = int(rval)
            if ins[0] == "add":
                registers[lval] += rval
            elif ins[0] == "mul":
                registers[lval] *= rval
            elif ins[0] == "div":
                registers[lval] //= rval
            elif ins[0] == "mod":
                registers[lval] %= rval
            elif ins[0] == "eql":
                registers[lval] = 1 if registers[lval] == rval else 0
    return registers[w]


