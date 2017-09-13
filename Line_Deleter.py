def process_lines(lines, line_length):
    processed_lines = []

    for i in range(len(lines)):
        if len(lines[i]) >= line_length:
            processed_lines.append(lines[i])
    return processed_lines


def save_to_file(filename, lines):
    with open(filename, "w") as f:
        f.write("\n".join(lines))

    return "Lines Processed"


def line_delete(filename, line_length):
    with open(filename)as f:
        line_data = f.read()
    line_data = line_data.splitlines()
    print(save_to_file(filename, process_lines(line_data, line_length)))

file_name = input('filename:')
min_characters = int(input('smallest line to keep:'))
line_delete(file_name, min_characters)
