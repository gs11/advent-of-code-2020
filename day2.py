import re
import utils


def is_valid_sled_rental(param1, param2, character, password):
    return password.count(character) >= param1 and password.count(character) <= param2


def is_valid_toboggan(param1, param2, character, password):
    return (password[param1 - 1] == character) != (password[param2 - 1] == character)


def find_valid_passwords(policy_passwords, is_valid_func):
    no_valid_passwords = 0
    for policy_password in policy_passwords:
        match = re.match(r'(\d+)-(\d+) (.): (.*)', policy_password)
        param1, param2, character, password = int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)

        if is_valid_func(param1, param2, character, password):
            no_valid_passwords += 1

    return no_valid_passwords


if __name__ == '__main__':
    policy_passwords = utils.read_file_lines('day2.test')
    assert find_valid_passwords(policy_passwords, is_valid_sled_rental) == 2
    assert find_valid_passwords(policy_passwords, is_valid_toboggan) == 1

    policy_passwords = utils.read_file_lines('day2.input')
    print(find_valid_passwords(policy_passwords, is_valid_sled_rental))
    print(find_valid_passwords(policy_passwords, is_valid_toboggan))
