import utils
import re

REQUIRED_PASSPORT_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
VALID_EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def read_passwords(filename):
    dict_passports = []
    passports = [passport.split() for passport in utils.read_file_lines(filename, '\n\n')]
    for passport in passports:
        dict_passport = {}
        for passport_part in passport:
            key, value = passport_part.split(':')
            dict_passport[key] = value
        dict_passports.append(dict_passport)
    return dict_passports


def find_complete_passports(passports):
    valid_passports = []
    for passport in passports:
        if REQUIRED_PASSPORT_FIELDS.issubset(set(passport.keys())):
            valid_passports.append(passport)
    return valid_passports


def parse_height(height):
    match = re.match(r'^([0-9]+)([a-z]{2})$', height)
    if match:
        return match.groups()
    else:
        return None, None


def is_passport_valid(passport):
    if not 1920 <= int(passport['byr']) <= 2002:
        return False

    if not 2010 <= int(passport['iyr']) <= 2020:
        return False

    if not 2020 <= int(passport['eyr']) <= 2030:
        return False

    value, uom = parse_height(passport['hgt'])
    if value and uom:
        if uom == 'cm' and not 150 <= int(value) <= 193:
            return False
        if uom == 'in' and not 59 <= int(value) <= 76:
            return False
    else:
        return False

    if not re.match(r'^#[0-9a-z]{6}$', passport['hcl']):
        return False

    if passport['ecl'] not in VALID_EYE_COLORS:
        return False

    if not re.match(r'^[0-9]{9}$', passport['pid']):
        return False

    return True


def count_valid_passports(passports):
    valid_passports = 0
    for passport in passports:
        if is_passport_valid(passport):
            valid_passports += 1
    return valid_passports


if __name__ == '__main__':
    passports = read_passwords('day4.test')
    complete_passports = find_complete_passports(passports)
    assert len(complete_passports) == 2

    passports = read_passwords('day4.test2')
    complete_passports = find_complete_passports(passports)
    assert count_valid_passports(complete_passports) == 4

    passports = read_passwords('day4.input')
    complete_passports = find_complete_passports(passports)
    print(len(complete_passports))
    print(count_valid_passports(complete_passports))
