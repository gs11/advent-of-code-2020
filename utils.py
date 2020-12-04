def read_file_lines(filename, split_by='\n'):
    with open(filename, 'r') as data:
        return data.read().split(split_by)
