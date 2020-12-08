import re
import utils


def parse_instructions(lines):
    instructions = []
    for line in lines:
        operation, argument = re.match(r'(.*) (.*)', line).groups()
        instructions.append((operation, int(argument)))
    return instructions


def execute_instructions(instructions, corrupted_instruction_position=None):
    visited_positions = []
    current_position = 0
    accumulator = 0

    while True:
        visited_positions.append(current_position)
        operation, argument = instructions[current_position]
        if current_position == corrupted_instruction_position and operation == 'nop':
            operation = 'jmp'
        elif current_position == corrupted_instruction_position and operation == 'jmp':
            operation = 'nop'

        if operation == 'acc':
            accumulator += argument
            current_position += 1
        elif operation == 'jmp':
            current_position += argument
        elif operation == 'nop':
            current_position += 1
        if current_position in visited_positions:
            return(1, accumulator)
        elif current_position == len(instructions):
            return (0, accumulator)


def repair_instructions(instructions):
    possibly_corrupted_positions = []
    for position in range(0, len(instructions)):
        if instructions[position][0] in ['nop', 'jmp']:
            possibly_corrupted_positions.append(position)

    for possibly_corrupted_position in possibly_corrupted_positions:
        return_code, accumulator = execute_instructions(instructions, possibly_corrupted_position)
        if return_code == 0:
            return accumulator


if __name__ == '__main__':
    lines = utils.read_file_lines('input/day08.test')
    instructions = parse_instructions(lines)
    assert execute_instructions(instructions) == (1, 5)
    assert repair_instructions(instructions) == 8

    lines = utils.read_file_lines('input/day08.input')
    instructions = parse_instructions(lines)
    print(execute_instructions(instructions)[1])
    print(repair_instructions(instructions))
