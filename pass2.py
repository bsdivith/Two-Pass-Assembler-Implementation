# pass2.py

def pass2(assembly_code, symbol_table):
    object_code = []

    for line in assembly_code:
        parts = line.strip().split()
        label, instruction, operands = None, None, []

        if len(parts) >= 1:
            label = parts[0]
        if len(parts) >= 2:
            instruction = parts[1]
        if len(parts) >= 3:
            operands = parts[2:]

        if instruction:
            if instruction == 'MOV':
                opcode = '01'
            elif instruction == 'ADD':
                opcode = '02'
            elif instruction == 'SUB':
                opcode = '03'
            elif instruction == 'HALT':
                opcode = 'FF'
            else:
                opcode = '00'  # Invalid instruction

            for i, operand in enumerate(operands):
                if operand in symbol_table:
                    operands[i] = str(symbol_table[operand])

            object_code.append(opcode + ''.join(operands))

    return object_code
