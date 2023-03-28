def read_file(file_name):
    lines = []
    with open(file_name) as file:
        for line in file:
            lines.append(line.replace('\n', ''))
            # _, *name = line.split(' ')
            # print(name)
    return lines


def choose_lines_with_word(lines, word):
    right_lines = []
    for line in lines:
        for word_in_line in line.split(' '):
            if word == word_in_line:
                right_lines.append(line)
                continue
    return right_lines


file = read_file("test.txt")
lines = choose_lines_with_word(file, 'Mary')
print(lines)
