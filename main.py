def read_file(file_name):
    lines = []
    with open(file_name) as file:
        for line in file:
            lines.append(line.replace('\n', ''))
    return lines


def choose_lines_with_word(lines, word):
    lines_with_word = []
    for line in lines:
        for word_in_line in line.split(' '):
            if word == word_in_line:
                lines_with_word.append(line)
                continue
    return lines_with_word


def write_to_file(lines):
    with open("result.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    file = read_file("test.txt")
    lines = choose_lines_with_word(file, 'Mary')
    write_to_file(lines)
    file = read_file("result.txt")
    print(file)
