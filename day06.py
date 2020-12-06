import utils


def count_yes_answers(groups):
    return sum(len(set(''.join(group))) for group in groups)


def count_unanimous_answers(groups):
    return sum(len(set(group[0]).intersection(*group)) for group in groups)


if __name__ == '__main__':
    groups = [group.split('\n') for group in utils.read_file_lines('input/day06.test', '\n\n')]
    assert count_yes_answers(groups) == 11
    assert count_unanimous_answers(groups) == 6

    groups = [group.split('\n') for group in utils.read_file_lines('input/day06.input', '\n\n')]
    print(count_yes_answers(groups))
    print(count_unanimous_answers(groups))
