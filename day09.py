import utils


def is_sum_of(sum, numbers):
    for first_number_index, first_number in enumerate(numbers):
        for second_number in numbers[first_number_index + 1:]:
            if first_number + second_number == sum:
                return True
    return False


def find_invalid_number(numbers, preamble):
    current_position = preamble

    while current_position < len(numbers):
        current_number = numbers[current_position]
        if not is_sum_of(current_number, numbers[current_position - preamble: current_position]):
            return current_number
        current_position += 1


def find_invalid_number_min_max_sum(numbers, invalid_number):
    range_start = 0
    range_end = 1
    while sum(numbers[range_start:range_end]) != invalid_number:
        while sum(numbers[range_start:range_end]) <= invalid_number:
            if sum(numbers[range_start:range_end]) == invalid_number:
                return min(numbers[range_start:range_end]) + max(numbers[range_start:range_end])
            range_end += 1
        range_start += 1
        range_end = range_start + 1


if __name__ == '__main__':
    numbers = [int(number) for number in utils.read_file_lines('input/day09.test')]
    invalid_number = find_invalid_number(numbers, 5)
    assert invalid_number == 127
    assert find_invalid_number_min_max_sum(numbers, invalid_number) == 62

    numbers = [int(number) for number in utils.read_file_lines('input/day09.input')]
    invalid_number = find_invalid_number(numbers, 25)
    print(invalid_number)
    print(find_invalid_number_min_max_sum(numbers, invalid_number))
