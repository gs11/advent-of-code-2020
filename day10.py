import utils


def sort_and_prepare(adapters):
    adapters = set(adapters)
    adapters.add(0)
    adapters.add(max(adapters) + 3)
    return sorted(adapters)


def get_adapter_intervals_product(adapters):
    differences_1 = 0
    differences_3 = 0

    for index, adapter in enumerate(adapters):
        if index != 0:
            if adapter - adapters[index - 1] == 1:
                differences_1 += 1
            elif adapter - adapters[index - 1] == 3:
                differences_3 += 1
    return differences_1 * differences_3


def recurse_adapters(adapters, adapter, cache):
    if adapter in cache:
        return cache[adapter]
    else:
        no_child_recursions = 0
        for interval in [1, 2, 3]:
            if adapter + interval == max(adapters):
                no_child_recursions += 1
            elif adapter + interval in adapters:
                no_child_recursions += recurse_adapters(adapters, adapter + interval, cache)
        cache[adapter] = no_child_recursions
        return no_child_recursions


def count_combinations(adapters):
    cache = {}
    return recurse_adapters(adapters, min(adapters), cache)


if __name__ == '__main__':
    adapters = [int(number) for number in utils.read_file_lines('input/day10.test')]
    adapters = sort_and_prepare(adapters)
    assert get_adapter_intervals_product(adapters) == 35
    assert count_combinations(adapters) == 8

    adapters = [int(number) for number in utils.read_file_lines('input/day10.test2')]
    adapters = sort_and_prepare(adapters)
    assert get_adapter_intervals_product(adapters) == 220
    assert count_combinations(adapters) == 19208

    adapters = [int(number) for number in utils.read_file_lines('input/day10.input')]
    adapters = sort_and_prepare(adapters)
    print(get_adapter_intervals_product(adapters))
    print(count_combinations(adapters))
