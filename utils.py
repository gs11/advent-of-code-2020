def read_file_lines(filename):
    with open(filename, 'r') as data:
        return data.read().splitlines()
