# pass1.py

def pass1(assembly_code):
    symbol_table = {}
    location_counter = 0

    for line in assembly_code:
        parts = line.strip().split()
        label, instruction, operands = None, None, []

        if len(parts) >= 1:
            label = parts[0]
        if len(parts) >= 2:
            instruction = parts[1]
        if len(parts) >= 3:
            operands = parts[2:]

        if label:
            symbol_table[label] = location_counter
        if instruction and instruction != 'DATA':
            location_counter += 1

    return symbol_table
