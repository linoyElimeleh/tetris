from entity.grid import Board
from entity.shape import match_entity_to_shape_object
from file_utils.file_service import get_lines, get_entries_in_line, writing_to_output_file


def tetris_engine(input_file, output_file):
    # Process the text file and extract the lines.
    lines = get_lines(input_file)

    # Read the input file line by line.
    for line in lines:

        # Initialize an empty 10*10 grid.
        board = Board()

        # Extract the entries in the line.
        entries = get_entries_in_line(line)

        remaining_height = 0

        for entry in entries:
            # Extract the shape and position for each entry
            shape, position = entry[0], int(entry[1])

            # Proces piece in the grid
            # Determine the height of the piece based on its shape letter.
            shape = match_entity_to_shape_object(shape)

            # Adding its height to the grid
            remaining_height = board.add_shape(shape, position).current_height

        # Print the summery
        writing_to_output_file(output_file, line, remaining_height, board)
