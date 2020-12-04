import utils


def find_entries(entries, number_of_entries):
    for first_entry_index, first_entry in enumerate(entries):
        for second_entry_index, second_entry in enumerate(entries[first_entry_index + 1:]):
            if number_of_entries == 2:
                if first_entry + second_entry == 2020:
                    return first_entry * second_entry
            elif number_of_entries == 3:
                for third_entry in entries[second_entry_index + 1:]:
                    if first_entry + second_entry + third_entry == 2020:
                        return first_entry * second_entry * third_entry


if __name__ == '__main__':
    entries = [int(entry) for entry in utils.read_file_lines('input/day01.test')]
    assert find_entries(entries, 2) == 514579
    assert find_entries(entries, 3) == 241861950

    entries = [int(entry) for entry in utils.read_file_lines('input/day01.input')]
    print(find_entries(entries, 2))
    print(find_entries(entries, 3))
