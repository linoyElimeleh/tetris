from const.grid import COLUMNS, ROWS, NONE_ELEMENT


class Board:
    def __init__(self):
        self.grid = self._initialize_grid()
        self.height_array = self._initialize_height_array()
        self.current_height = 0

    @staticmethod
    def _initialize_grid():
        grid = [[NONE_ELEMENT] * COLUMNS for _ in range(ROWS)]
        return grid

    @staticmethod
    def _initialize_height_array():
        height = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        return height

    def _get_number_row_to_start_with(self, position):
        return self.height_array[position]

    def _set_height(self, new_height):
        self.current_height = new_height

    def _set_height_array_in_place(self, place):
        self.height_array[place] += 1

    def _reduce_height_array(self):
        for column in range(COLUMNS):
            if self.height_array[column] != 0:
                self.height_array[column] -= 1

    def _insert_shape_into_grid(self, shape, row_number, column_number):

        # Reverse the shape metrics to we can insert easily to the grid
        shape_metrics = list(reversed(shape.matrix))

        row_in_shape_number = 0

        # Go over each row from the row we are starting with until the shape height
        for row in range(row_number, row_number + shape.height):
            column_in_shape_number = 0

            # Go over each column from the row we are starting with until the shape height
            for column in range(column_number, column_number + shape.width):

                # Check if the place in the shape metrix contains a letter
                if shape_metrics[row_in_shape_number][column_in_shape_number] == shape.letter:
                    # Insert into the grid the shape letter
                    self.grid[row][column] = shape_metrics[row_in_shape_number][column_in_shape_number]

                    # Update the height array, to know where to start next time
                    self._set_height_array_in_place(column)

                column_in_shape_number += 1

            row_in_shape_number += 1

        # Update the total height to summarize all
        self._set_height(row_number + shape.height)

    def _check_if_rows_are_filled(self, shape_height):

        # Check if any rows are filled and clear them
        filled_rows = [row for row in range(shape_height) if all(cell != NONE_ELEMENT for cell in self.grid[row])]
        for row in filled_rows:
            self.grid.pop(row)
            self.grid.insert(0, [NONE_ELEMENT] * 10)
            self._reduce_height_array()

        # If the filled row is different from zero, reduce the total height with the filled rows length
        if len(filled_rows) != 0:
            self._set_height(self.current_height - len(filled_rows))

    def _does_shape_fit_in_grid(self, shape, row_number, position):
        # Reverse the shape metrics to we can insert easily to the grid
        shape_metrics = list(reversed(shape.matrix))

        row_in_shape_number = 0

        # Go over each row from the row we are starting with until the shape height
        for row in range(row_number, row_number + shape.height):
            column_in_shape_number = 0

            # Go over each column from the row we are starting with until the shape height
            for column in range(position, position + shape.width):

                # Check if the place in the shape metrix contains a letter and the grid is not empty
                # Return false if it does not fit
                if ((shape_metrics[row_in_shape_number][column_in_shape_number] == shape.letter)
                        & (self.grid[row][column] != NONE_ELEMENT)):
                    return False

                column_in_shape_number += 1
            row_in_shape_number += 1

        # Return true if the condition in the function does not match even once. The shape is fitting.
        return True

    def add_shape(self, shape, position):

        # Check from where to start adding the new shape
        row_number_to_start_from = self._get_number_row_to_start_with(position)

        # Go over the rows from the place we need to start until the end of the rows
        for row_number in range(row_number_to_start_from, ROWS):

            # Check if the shape fit to the grid in the current position
            does_shape_fit_flag = self._does_shape_fit_in_grid(shape, row_number, position)
            if not does_shape_fit_flag:
                # If the shape does not fit to the position, continue up with rows to find new place
                continue

            # If the shape is fit, stop the process and insert the shape into the position
            self._insert_shape_into_grid(shape, row_number, position)
            break

        # Check if any rows are filled and clear them
        self._check_if_rows_are_filled(shape.height)

        return self

    def __str__(self):
        rows = []
        for row in reversed(self.grid):  # Reverse the order of the rows
            rows.append(''.join(str(cell) for cell in row))
        return '\n'.join(rows)
