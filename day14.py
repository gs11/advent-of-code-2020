import re
import utils


def apply_mask(value, mask):
    new_value = list(to_binary_string(value))
    for index, char in enumerate(mask):
        if char != 'X':
            new_value[index] = char
    return ''.join(new_value)


def apply_mask2(value, mask):
    new_value = list(to_binary_string(value))
    floating_bits = []
    for index, char in enumerate(mask):
        if char == '1':
            new_value[index] = '1'
        elif char == 'X':
            new_value[index] = 'X'
            floating_bits.append(index)
    return ''.join(new_value), floating_bits


def get_address_value(line):
    return re.match(r'mem\[(\d+)\] = (\d+)', line).groups()


def to_binary_string(value):
    return bin(int(value))[2:].zfill(36)


def update_address(address, index, value):
    updated_address = list(address)
    updated_address[index] = value
    return ''.join(updated_address)


def run_initializion_program(lines):
    memory = {}
    mask = None
    for line in lines:
        if line.startswith('mask'):
            mask = line[7:]
        else:
            address, value = get_address_value(line)
            memory[address] = int(apply_mask(value, mask), 2)

    return sum(memory.values())


def write_to_memory(memory, base_address, mask, floating_bits, value):
    floating_bit = floating_bits[0]

    for floating_bit_value in ['0', '1']:
        floating_bit_address = update_address(base_address, floating_bit, floating_bit_value)

        if len(floating_bits) == 1:
            memory[floating_bit_address] = int(value)
        else:
            write_to_memory(memory, floating_bit_address, mask, floating_bits[1:], value)


def run_initializion_program2(lines):
    memory = {}
    mask = None
    for line in lines:
        if line.startswith('mask'):
            mask = line[7:]
        else:
            address, value = get_address_value(line)
            base_address, floating_bits = apply_mask2(address, mask)
            write_to_memory(memory, base_address, mask, floating_bits, value)

    return sum(memory.values())


if __name__ == '__main__':
    lines = utils.read_file_lines('input/day14.test')
    assert run_initializion_program(lines) == 165
    lines = utils.read_file_lines('input/day14.test2')
    assert run_initializion_program2(lines) == 208

    lines = utils.read_file_lines('input/day14.input')
    print(run_initializion_program(lines))
    print(run_initializion_program2(lines))
