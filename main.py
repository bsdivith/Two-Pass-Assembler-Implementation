# main.py

from pass1 import pass1
from pass2 import pass2
from test_assembler import assembly_code

def create_txt(assembly_code, symbol_table, object_code):
    # Open or create a text file in write mode
    with open("assembler_output.txt", "a") as file:
        # Write sample assembly code
        file.write("Random Assembly Code:\n")
        for i, line in enumerate(assembly_code, 1):
            file.write(f"{i}. {line}\n")

        # Write symbol table
        file.write("\nSymbol Table:\n")
        for label, location in symbol_table.items():
            file.write(f"- {label}: {location}\n")

        # Write object code
        file.write("\nObject Code:\n")
        for i, code in enumerate(object_code, 1):
            file.write(f"{i}. {code}\n")
        file.write("--------------------------------------------\n")

# Run Pass 1 to build the symbol table
symbol_table = pass1(assembly_code)

# Run Pass 2 to generate object code
object_code = pass2(assembly_code, symbol_table)

# Create text file with assembly code, symbol table, and object code
create_txt(assembly_code, symbol_table, object_code)

# Display the symbol table
print("\nSymbol Table:")
for label, location in symbol_table.items():
    print(f"- {label}: {location}")
