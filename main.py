def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            print(line)


read_file("test.txt")

