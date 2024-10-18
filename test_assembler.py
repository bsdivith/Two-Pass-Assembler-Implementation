# test_assembler.py

import random
from pass1 import pass1
from pass2 import pass2

# Generate random assembly code
def generate_random_assembly_code(num_lines):
    assembly_code = []
    for _ in range(num_lines):
        instruction = random.choice(["MOV", "ADD", "SUB", "HALT"])
        operand = random.randint(0, 99)
        line = f"{instruction} A, {operand}"
        assembly_code.append(line)
    return assembly_code

# Generate random assembly code
num_lines = 5  # Number of lines of random assembly code
assembly_code = generate_random_assembly_code(num_lines)

# Display the random assembly code
print("Random Assembly Code:")
for line in assembly_code:
    print(line)

# Run Pass 1 to build the symbol table
symbol_table = pass1(assembly_code)

# Run Pass 2 to generate object code
object_code = pass2(assembly_code, symbol_table)

# Display the object code
print("\nObject Code:")
for code in object_code:
    print(code)
