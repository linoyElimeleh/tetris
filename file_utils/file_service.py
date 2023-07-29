def get_lines(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    return lines


def get_entries_in_line(line):
    line = line.strip()
    entries = line.split(',')

    return entries


def writing_to_output_file(output_file, line, remaining_height, board):
    with open(output_file, "a+") as file:
        file.write(f"""
               Input is: {line} 
               Remaining Height is: {remaining_height}
               Board is: 
               {board}
               ---- """)


def get_info_in_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
