import pandas as pd

# Step 1: Load Excel Sheet (RAM) into Python
file_path = "hexadecimalcodes.xlsx"  # Path to your Excel file
sheet_name = 0  # Default sheet is the first sheet
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Step 2: Fetch a Hexadecimal Instruction
# Assuming hexadecimal instructions are in the first column of the Excel sheet
instruction_index = 5 # Replace this with the desired row index
#iloc[] is a pandas method used to access specific elements 
#instruction_index defines row
hex_instruction = data.iloc[instruction_index, 0]#row,column

# Step 3: Convert Hexadecimal to 32-bit Binary
binary_instruction = bin(int(hex_instruction, 16))[2:].zfill(32)

# Output
print(f"Fetched Hexadecimal Instruction: {hex_instruction}")
print(f"Converted 32-bit Binary Instruction: {binary_instruction}")

operand1 = int(binary_instruction [0:8], 2)
operand2 = int(binary_instruction [8:16], 2)
opCode = int(binary_instruction [16:20], 2) 
alu_enable = int(binary_instruction [20:21], 2)
load_bit = int(binary_instruction [21:22], 2)
store_bit = int(binary_instruction [22:23], 2)
register_selection = int(binary_instruction [23:26], 2)
Reserved = binary_instruction[26:32]

result = 0
status = 0

# Checking the ALU enable flag
if alu_enable == 1:
    if opCode == 0:
        result = operand1 + operand2
    elif opCode == 1:
        result = operand1 - operand2
    elif opCode == 2:
        result = operand1 * operand2
    elif opCode == 3:
        result = operand1 / operand2 if operand2 != 0 else "Error: Division by Zero"
    elif opCode == 4:
        result = operand1 ** operand2 
    elif opCode == 5:
        result = operand1 +1
    elif opCode == 6:
        result = operand1 -1
    else:
        result = "Invalid Operator"
    status = 1
else:
    result = "ALU Disabled"

register = result
registers = [0] * 8  # Assume 8 registers, initialized to 0
if load_bit == 1 and store_bit == 0:
    registers[register_selection] = operand1
    print(f"Operand1 stored in Register {register_selection}: {registers[register_selection]}")
elif store_bit == 1 and load_bit == 0:
    registers[register_selection] = result
    print(f"result stored in Register {register_selection}: {registers[register_selection]}")
elif store_bit == 1 and load_bit == 1:
    result_register = (register_selection + 1) % 8
    registers[result_register] = result
    print(f"Result stored in Register {result_register}: {registers[result_register]}")



print(f"Binary Instruction: {binary_instruction }")
print(f"Operand 1: {operand1}")
print(f"Operand 2: {operand2}")
print(f"ALU Enable: {alu_enable}")
print(f"Opcode: {opCode}")
print(f"Register list: {registers}")
print(f"Reserved Bits: {Reserved}")
print(f"load bit {load_bit}")
print(f"store bit {store_bit}")
print(f"Result: {result}")
print(f"Status: {status}")

