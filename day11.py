from copy import deepcopy
import utils

UNOCCUPIED = 'L'
OCCUPIED = '#'


def parse_waiting_area(lines):
    waiting_area = {}
    for line_index, line in enumerate(lines):
        waiting_area[line_index] = {}
        for column_index, seat in enumerate(line):
            waiting_area[line_index][column_index] = seat
    return waiting_area


def count_adjacent_occupied_seats(waiting_area, y, x):
    adjacent_occupied_seats = 0

    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            try:
                if (y_offset != 0 or x_offset != 0) and waiting_area[y + y_offset][x + x_offset] == OCCUPIED:
                    adjacent_occupied_seats += 1
            except KeyError:
                pass  # Out of bounds, ignore
    return adjacent_occupied_seats


def count_visible_occupied_seats(waiting_area, y, x):
    visible_occupied_seats = 0

    for y_angle in range(-1, 2):
        for x_angle in range(-1, 2):
            y_offset = y_angle
            x_offset = x_angle
            while y_angle != 0 or x_angle != 0:
                try:
                    if waiting_area[y + y_offset][x + x_offset] == OCCUPIED:
                        visible_occupied_seats += 1
                        break
                    elif waiting_area[y + y_offset][x + x_offset] == UNOCCUPIED:
                        break
                    y_offset += y_angle
                    x_offset += x_angle
                except KeyError:
                    break  # Out of bounds and no seat found, break

    return visible_occupied_seats


def count_occupied_seats(waiting_area):
    occupied_seats = 0
    for y in waiting_area:
        occupied_seats += list(waiting_area[y].values()).count(OCCUPIED)
    return occupied_seats


def shift_waiting_area_until_stable(waiting_area, adjacent_func, unoccupy_threshold):
    while True:
        shifted_waiting_area = deepcopy(waiting_area)
        for y in waiting_area:
            for x in waiting_area[y]:
                relevant_occupied_seats = adjacent_func(waiting_area, y, x)
                if waiting_area[y][x] == UNOCCUPIED and relevant_occupied_seats == 0:
                    shifted_waiting_area[y][x] = OCCUPIED
                elif waiting_area[y][x] == OCCUPIED and relevant_occupied_seats >= unoccupy_threshold:
                    shifted_waiting_area[y][x] = UNOCCUPIED

        if shifted_waiting_area == waiting_area:
            break
        else:
            waiting_area = shifted_waiting_area

    return count_occupied_seats(shifted_waiting_area)


if __name__ == '__main__':
    waiting_area = parse_waiting_area(utils.read_file_lines('input/day11.test'))
    assert shift_waiting_area_until_stable(waiting_area, count_adjacent_occupied_seats, 4) == 37
    assert shift_waiting_area_until_stable(waiting_area, count_visible_occupied_seats, 5) == 26

    waiting_area = parse_waiting_area(utils.read_file_lines('input/day11.input'))
    print(shift_waiting_area_until_stable(waiting_area, count_adjacent_occupied_seats, 4))
    print(shift_waiting_area_until_stable(waiting_area, count_visible_occupied_seats, 5))
