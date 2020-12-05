import utils


def traverse_binary_tree(tree, min_char, max_char):
    current_range = (0, 2 ** len(tree) - 1)
    for index in range(0, len(tree)):
        min_val, max_val = current_range
        vals_in_new_range = max_val - min_val + 1
        if tree[index] == min_char:
            max_val = min_val + (vals_in_new_range / 2) - 1
        else:
            min_val = max_val - (vals_in_new_range / 2) + 1
        current_range = (min_val, max_val)
    return int(current_range[0])


def get_seat_id(boarding_pass):
    row = traverse_binary_tree(boarding_pass[0:7], 'F', 'B')
    column = traverse_binary_tree(boarding_pass[7:10], 'L', 'R')
    return row * 8 + column


def get_seat_ids(boarding_passes):
    return [get_seat_id(boarding_pass) for boarding_pass in boarding_passes]


def find_missing_seat_id(seat_ids):
    all_seat_ids = [seat_id for seat_id in range(min(seat_ids), max(seat_ids) + 1)]
    return set(all_seat_ids).difference(set(seat_ids)).pop()


if __name__ == '__main__':
    boarding_passes = utils.read_file_lines('input/day05.test')
    assert max(get_seat_ids(boarding_passes)) == 820

    boarding_passes = utils.read_file_lines('input/day05.input')
    seat_ids = get_seat_ids(boarding_passes)
    print(max(seat_ids))
    print(find_missing_seat_id(seat_ids))
