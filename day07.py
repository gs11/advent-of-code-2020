import re
import utils


STARTING_BAG = 'shiny gold'


def load_bags(rules):
    enclosing_bags = {}
    for rule in rules:
        enclosing_bag, contains = re.match(r'(.*) bags contain (.*).', rule).groups()
        if contains == 'no other bags':
            enclosing_bags[enclosing_bag] = []
        else:
            enclosing_bags[enclosing_bag] = []
            for bag in contains.split(', '):
                quantity, color = re.match(r'(\d+) (.*) bag', bag).groups()
                for _ in range(0, int(quantity)):
                    enclosing_bags[enclosing_bag].append(color)
    return enclosing_bags


def get_enclosing_bags(bags, color):
    enclosing_bags = []
    for enclosing_bag, bags in bags.items():
        if color in bags:
            enclosing_bags.append(enclosing_bag)
    return enclosing_bags


def recurse_enclosing_bags(bags, bag, seen_bags):
    if bag != STARTING_BAG:
        seen_bags.add(bag)
    for enclosing_bag in get_enclosing_bags(bags, bag):
        if enclosing_bag not in seen_bags:
            recurse_enclosing_bags(bags, enclosing_bag, seen_bags)


def count_enclosing_bags(bags):
    seen_bags = set()
    recurse_enclosing_bags(bags, STARTING_BAG, seen_bags)
    return(len(seen_bags))


def recurse_enclosed_bags(bags, enclosing_bag, enclosed_bags):
    for bag in bags[enclosing_bag]:
        enclosed_bags.append(bag)
        recurse_enclosed_bags(bags, bag, enclosed_bags)


def count_enclosed_bags(bags):
    enclosed_bags = []
    recurse_enclosed_bags(bags, STARTING_BAG, enclosed_bags)
    return len(enclosed_bags)


if __name__ == '__main__':
    rules = utils.read_file_lines('input/day07.test')
    bags = load_bags(rules)
    assert count_enclosing_bags(bags) == 4
    assert count_enclosed_bags(bags) == 32

    rules = utils.read_file_lines('input/day07.test2')
    bags = load_bags(rules)
    assert count_enclosed_bags(bags) == 126

    rules = utils.read_file_lines('input/day07.input')
    bags = load_bags(rules)
    print(count_enclosing_bags(bags))
    print(count_enclosed_bags(bags))
