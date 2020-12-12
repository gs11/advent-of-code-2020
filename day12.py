import math
import re
import utils


DIRECTION_DEGREES_XREF = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270
}


def parse_instructions(lines):
    instructions = []
    for line in lines:
        action, value = re.match(r'(.)(\d+)', line).groups()
        instructions.append((action, int(value)))
    return instructions


def travel(instructions):
    heading = 90
    ship_x = 0
    ship_y = 0

    for instruction in instructions:
        action, value = instruction

        if action == 'L':
            heading = (heading - value) % 360
        elif action == 'R':
            heading = (heading + value) % 360
        else:
            if action == 'F':
                course = heading
            else:
                course = DIRECTION_DEGREES_XREF[action]

            ship_x += int(math.sin(math.radians(course)) * value)
            ship_y += int(math.cos(math.radians(course)) * value)

    return abs(ship_x) + abs(ship_y)


def rotate_waypoint(waypoint_x_offset, waypoint_y_offset, degrees):
    for _ in range(int(degrees / 90)):
        previous_waypoint_x_offset = waypoint_x_offset
        waypoint_x_offset = waypoint_y_offset
        waypoint_y_offset = -previous_waypoint_x_offset
    return waypoint_x_offset, waypoint_y_offset


def travel_with_waypoint(instructions):
    ship_x = 0
    ship_y = 0
    waypoint_x_offset = 10
    waypoint_y_offset = 1

    for instruction in instructions:
        action, value = instruction

        if action == 'F':
            ship_x += waypoint_x_offset * value
            ship_y += waypoint_y_offset * value
        elif action == 'L':
            waypoint_x_offset, waypoint_y_offset = rotate_waypoint(waypoint_x_offset, waypoint_y_offset, 360 - value)
        elif action == 'R':
            waypoint_x_offset, waypoint_y_offset = rotate_waypoint(waypoint_x_offset, waypoint_y_offset, value)
        else:
            new_waypoint_degrees = DIRECTION_DEGREES_XREF[action]
            waypoint_x_offset += int(math.sin(math.radians(new_waypoint_degrees)) * value)
            waypoint_y_offset += int(math.cos(math.radians(new_waypoint_degrees)) * value)

    return abs(ship_x) + abs(ship_y)


if __name__ == '__main__':
    instructions = parse_instructions(utils.read_file_lines('input/day12.test'))
    assert travel(instructions) == 25
    assert travel_with_waypoint(instructions) == 286

    instructions = parse_instructions(utils.read_file_lines('input/day12.input'))
    print(travel(instructions))
    print(travel_with_waypoint(instructions))
