import sys
import os

if (len(sys.argv) > 1) and (os.path.splitext(sys.argv[1])[1] == '.rizz'):
    file_path = sys.argv[1]
    try:

        with open(file_path, 'r') as file:
            program = file.read()
    except Exception as e:
        print(e)
else:
    print("\u001b[31mPlease provide a .rizz file as an argument.")
    exit()

tape = [0]
cell_index = 0
user_input = []
loop_table = {}
loop_stack = []

# Building loop table
for ip, instruction in enumerate(program):
    if instruction == "{":
        loop_stack.append(ip)
    elif instruction == "}":
        loop_beginning_index = loop_stack.pop()
        loop_table[loop_beginning_index] = ip
        loop_table[ip] = loop_beginning_index

ip = 0
while ip < len(program):
    instruction = program[ip]  # creating the instruction variable
    if instruction == "I":
        tape[cell_index] += 1
        if tape[cell_index] == 256:
            tape[cell_index] = 0
    elif instruction == "R":
        tape[cell_index] -= 1
        if tape[cell_index] == -1:
            tape[cell_index] = 255
    elif instruction == "<":
        cell_index -= 1
        if cell_index == -1:
            tape.insert(0, 0)
            cell_index = 0
    elif instruction == ">":
        cell_index += 1
        if cell_index == len(tape):
            tape.append(0)
    elif instruction == "Z":
        print(chr(tape[cell_index]), end="")
    elif instruction == ",":
        if user_input == []:
            user_input = list(input() + "\n")
        tape[cell_index] = ord(user_input.pop(0))
    elif instruction == "{":
        if not tape[cell_index]:
            ip = loop_table[ip]
    elif instruction == "}":
        if tape[cell_index]:
            ip = loop_table[ip]
    ip += 1

    # The code below helps debug the code above. Only uncomment if you're debugging broken code.
    # print(f"ip: {ip}, instruction: {instruction}, tape: {tape}")


# 69 Lines, Yessir ;)