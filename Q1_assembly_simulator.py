# Q1: Simulate simple assembly instructions using registers and memory

# Memory: address -> value
memory = {100: 12, 104: 8}

# Registers start at 0
registers = {"R1": 0, "R2": 0, "R3": 0}

# Program: list of (operation, operands)
program = [
    ("LOAD", "R1", 100),
    ("LOAD", "R2", 104),
    ("ADD", "R3", "R1", "R2"),
    ("STORE", "R3", 108),
]

print("Initial memory:", memory)
print("-" * 40)

for step, instr in enumerate(program, start=1):
    op = instr[0]

    if op == "LOAD":
        reg, addr = instr[1], instr[2]
        print(f"Step {step}: LOAD {reg}, {addr}")
        registers[reg] = memory[addr]

    elif op == "ADD":
        dest, src1, src2 = instr[1], instr[2], instr[3]
        print(f"Step {step}: ADD {dest}, {src1}, {src2}")
        registers[dest] = registers[src1] + registers[src2]

    elif op == "STORE":
        reg, addr = instr[1], instr[2]
        print(f"Step {step}: STORE {reg}, {addr}")
        memory[addr] = registers[reg]

    print("   Registers:", registers)

print("-" * 40)
print("Final register contents:")
for name, value in registers.items():
    print(f"  {name} = {value}")

print(f"Final contents of memory location 108: M[108] = {memory[108]}")
