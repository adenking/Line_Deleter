def process_lines(lines, line_length):
    processed_lines = []
    j = 0
    for i in len(lines):
        if len(i) > line_length:
            processed_lines[j] = lines[i]
            j += 1
    return processed_lines


def line_delete(filename, line_length):
    with open(filename)as f:
        line_data = f.read()
    line_data = line_data.splitlines()
    print(process_lines(line_data, line_length))


line_delete("wordlist_test.txt", 3)
