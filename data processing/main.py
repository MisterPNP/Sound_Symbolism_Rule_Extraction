# want to take in file line by line
# make tuples from these lines
# process each tuple elements

def process_line(line):
    translation_table = dict.fromkeys(map(ord, '/ '), None)
    line = line.split()
    line = tuple((line[0], line[1].translate(translation_table)))
    return line


def format_file(input_file):
    data = []
    lines = input_file.readlines()
    for line in lines:
        if line[0] != "\'":
            tuple_line = process_line(line)
            data.append(tuple_line)

    return data


if __name__ == '__main__':
    file = open('../Data/IPA Data/en_US.txt', 'r', encoding='utf8')
    data = format_file(file)

    print(data)

    file.close()
