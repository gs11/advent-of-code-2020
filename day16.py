import math
import re
import utils


RULE_REGEX = r'(.*): (\d+)-(\d+) or (\d+)-(\d+)'


def parse_input_sections(input_sections):
    rules = {}
    for rule in input_sections[0].split('\n'):
        rule_name, range1_min, range1_max, range2_min, range2_max = re.match(RULE_REGEX, rule).groups()
        rules[rule_name] = ((int(range1_min), int(range1_max), int(range2_min), int(range2_max)))

    my_ticket = input_sections[1].split('\n')[1].split(',')
    nearby_tickets = [nearby_ticket.split(',') for nearby_ticket in input_sections[2].split('\n')[1:]]

    return rules, my_ticket, nearby_tickets


def is_value_valid(rules, value):
    for rule in rules.values():
        range1_min, range1_max, range2_min, range2_max = rule
        if range1_min <= value <= range1_max or range2_min <= value <= range2_max:
            return True
    return False


def get_ticket_invalid_values(rules, ticket):
    invalid_values = []
    for value in ticket:
        if not is_value_valid(rules, int(value)):
            invalid_values.append(int(value))
    return invalid_values


def sum_invalid_ticket_values(rules, tickets):
    invalid_values = []
    for ticket in tickets:
        invalid_values.extend(get_ticket_invalid_values(rules, ticket))
    return sum(invalid_values)


def filter_valid_tickets(rules, tickets):
    valid_tickets = []
    for ticket in tickets:
        ticket_invalid_values = get_ticket_invalid_values(rules, ticket)
        if not ticket_invalid_values:
            valid_tickets.append(ticket)
    return valid_tickets


def get_value_indexes(rules, tickets, field_prefix=''):
    value_index_rules = {}
    for index in range(len(tickets[0])):
        for rule_name, rule in rules.items():
            all_tickets_values_valid_for_rule = True
            for ticket in tickets:
                if not is_value_valid({'_': rule}, int(ticket[index])):
                    all_tickets_values_valid_for_rule = False
                    break
            if all_tickets_values_valid_for_rule:
                if index not in value_index_rules:
                    value_index_rules[index] = []
                value_index_rules[index].append(rule_name)

    value_index_rules = dict(sorted(value_index_rules.items(), key=lambda item: len(item[1])))

    index_field_xref = {}
    seen_ticket_fields = []
    for index, matching_rules in value_index_rules.items():
        field = list(set(matching_rules) - set(seen_ticket_fields))[0]
        index_field_xref[index] = field
        seen_ticket_fields.append(field)

    return [index for index, field in index_field_xref.items() if field.startswith(field_prefix)]


def get_ticket_value_product(ticket, value_indexes):
    ticket_values = [int(value) for index, value in enumerate(ticket) if index in value_indexes]
    return math.prod(ticket_values)


if __name__ == '__main__':
    input_sections = utils.read_file_lines('input/day16.test', '\n\n')
    rules, my_ticket, nearby_tickets = parse_input_sections(input_sections)
    assert sum_invalid_ticket_values(rules, nearby_tickets) == 71

    input_sections = utils.read_file_lines('input/day16.test2', '\n\n')
    rules, my_ticket, nearby_tickets = parse_input_sections(input_sections)
    value_indexes = get_value_indexes(rules, filter_valid_tickets(rules, nearby_tickets))
    assert get_ticket_value_product(my_ticket, value_indexes) == 1716

    input_sections = utils.read_file_lines('input/day16.input', '\n\n')
    rules, my_ticket, nearby_tickets = parse_input_sections(input_sections)
    print(sum_invalid_ticket_values(rules, nearby_tickets))
    value_indexes = get_value_indexes(rules, filter_valid_tickets(rules, nearby_tickets), 'departure')
    print(get_ticket_value_product(my_ticket, value_indexes))
