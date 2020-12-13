import math
import utils


def parse_bus_data(lines):
    earliest_departure, bus_ids = lines
    earliest_departure = int(earliest_departure)
    bus_ids = [int(bus_id) if bus_id.isdigit() else bus_id for bus_id in bus_ids.split(',')]
    return int(earliest_departure), bus_ids


def get_int_bus_ids(bus_ids):
    return list(filter(lambda bus_id: isinstance(bus_id, int), bus_ids))


def get_earliest_bus(earliest_departure, bus_ids):
    while True:
        for bus_id in bus_ids:
            if bus_id != 'x' and earliest_departure % bus_id == 0:
                return earliest_departure, bus_id
        earliest_departure += 1


def find_sequence_of_buses(bus_ids):
    first_bus_departure = 0
    current_timestamp = 0
    current_bus_id_index = 1

    while current_bus_id_index < len(bus_ids):
        current_bus_id = bus_ids[current_bus_id_index]

        if current_bus_id == 'x' or current_timestamp % current_bus_id == 0:
            # OK, next bus
            current_bus_id_index += 1
        else:
            # Not ok, start with the first bus again but skip the product of all bus ids currently in the correct sequence
            first_bus_departure += math.prod(get_int_bus_ids(bus_ids[0:current_bus_id_index]))
            current_timestamp = first_bus_departure
            current_bus_id_index = 1
        current_timestamp += 1

    return first_bus_departure


if __name__ == '__main__':
    earliest_departure, bus_ids = parse_bus_data(utils.read_file_lines('input/day13.test'))
    bus_departure, departing_bus_id = get_earliest_bus(earliest_departure, bus_ids)
    assert (bus_departure - earliest_departure) * departing_bus_id == 295
    assert find_sequence_of_buses(bus_ids) == 1068781
    assert find_sequence_of_buses([17, 'x', 13, 19]) == 3417
    assert find_sequence_of_buses([67, 7, 59, 61]) == 754018
    assert find_sequence_of_buses([67, 'x', 7, 59, 61]) == 779210
    assert find_sequence_of_buses([67, 7, 'x', 59, 61]) == 1261476
    assert find_sequence_of_buses([1789, 37, 47, 1889]) == 1202161486

    earliest_departure, bus_ids = parse_bus_data(utils.read_file_lines('input/day13.input'))
    bus_departure, departing_bus_id = get_earliest_bus(earliest_departure, bus_ids)
    print((bus_departure - earliest_departure) * departing_bus_id)
    print(find_sequence_of_buses(bus_ids))
