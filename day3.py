import utils


def traverse_map(tree_map, x_speed, y_speed):
    encountered_trees = 0

    current_x = 0
    for current_y in range(0, len(tree_map), y_speed):
        if tree_map[current_y][current_x % len(tree_map[0])] == '#':
            encountered_trees += 1
        current_x += x_speed

    return encountered_trees


if __name__ == '__main__':
    tree_map = utils.read_file_lines('day3.test')
    assert traverse_map(tree_map, 3, 1) == 7
    slopes_product = traverse_map(tree_map, 1, 1)
    slopes_product *= traverse_map(tree_map, 3, 1)
    slopes_product *= traverse_map(tree_map, 5, 1)
    slopes_product *= traverse_map(tree_map, 7, 1)
    slopes_product *= traverse_map(tree_map, 1, 2)
    assert slopes_product == 336

    tree_map = utils.read_file_lines('day3.input')
    print(traverse_map(tree_map, 3, 1))
    slopes_product = traverse_map(tree_map, 1, 1)
    slopes_product *= traverse_map(tree_map, 3, 1)
    slopes_product *= traverse_map(tree_map, 5, 1)
    slopes_product *= traverse_map(tree_map, 7, 1)
    slopes_product *= traverse_map(tree_map, 1, 2)
    print(slopes_product)
