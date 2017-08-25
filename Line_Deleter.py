def process_lines(lines, line_length):
    proccessed_lines = []
    j = 0
    for i in range(0, len(lines)):
        if len(i) > line_length:
            proccessed_lines[j] += lines[i]
            j += 1
    return proccessed_lines


def line_delete(filename, line_length):
    with open(filename)as f:
        print(process_lines(f.read(), line_length))



line_delete("wordlist_test.txt", 3)
