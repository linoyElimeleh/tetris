from datetime import datetime

import pytest

from entity.grid import Board, COLUMNS, ROWS
from entity.shape import match_entity_to_shape_object, T, J, S, Z, L, I, Q
from file_utils.file_service import get_info_in_file
from tetris_engine import tetris_engine


@pytest.fixture
def empty_board():
    return Board()


def test_board_initialization(empty_board):
    assert len(empty_board.grid) == ROWS
    assert len(empty_board.grid[0]) == COLUMNS
    assert empty_board.current_height == 0
    assert empty_board.height_array == [0] * COLUMNS


def test_shape_initialization():
    assert T.letter == 'T'
    assert T.matrix == [['T', 'T', 'T'],
                        ['', 'T', '']]
    assert T.height == 2
    assert T.width == 3

    assert T.letter == 'T'
    assert T.matrix == [['T', 'T', 'T'],
                        ['', 'T', '']]
    assert T.height == 2
    assert T.width == 3

    assert S.letter == 'S'
    assert S.matrix == [['', 'S', 'S'],
                        ['S', 'S', '']]
    assert S.height == 2
    assert S.width == 3

    assert Z.letter == 'Z'
    assert Z.matrix == [['Z', 'Z', ''],
                        ['', 'Z', 'Z']]
    assert Z.height == 2
    assert Z.width == 3

    assert J.letter == 'J'
    assert J.matrix == [['', 'J'],
                        ['', 'J'],
                        ['J', 'J']]
    assert J.height == 3
    assert J.width == 2

    assert L.letter == 'L'
    assert L.matrix == [['L', ''],
                        ['L', ''],
                        ['L', 'L']]
    assert L.height == 3
    assert L.width == 2

    assert I.letter == 'I'
    assert I.matrix == [['I', 'I', 'I', 'I']]
    assert I.height == 1
    assert I.width == 4

    assert Q.letter == 'Q'
    assert Q.matrix == [['Q', 'Q'],
                        ['Q', 'Q']]
    assert Q.height == 2
    assert Q.width == 2


def test_match_entity_to_shape_object():
    assert match_entity_to_shape_object('T') == T
    assert match_entity_to_shape_object('S') == S
    assert match_entity_to_shape_object('Z') == Z
    assert match_entity_to_shape_object('J') == J
    assert match_entity_to_shape_object('L') == L
    assert match_entity_to_shape_object('I') == I
    assert match_entity_to_shape_object('Q') == Q
    assert match_entity_to_shape_object('X') is None


def test_add_one_shape_to_empty_board_sanity_test(empty_board):
    empty_board.add_shape(T, 0)

    assert empty_board.current_height == 2
    assert empty_board.height_array == [1, 2, 1, 0, 0, 0, 0, 0, 0, 0]
    assert empty_board.grid == [['#', 'T', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['T', 'T', 'T', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]


def test_add_shape_with_collision(empty_board):
    empty_board.add_shape(T, 0)
    empty_board.add_shape(S, 1)

    assert empty_board.current_height == 4
    assert empty_board.height_array == [1, 3, 3, 1, 0, 0, 0, 0, 0, 0]
    assert empty_board.grid == [['#', 'T', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['T', 'T', 'T', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', 'S', 'S', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', 'S', 'S', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]


def test_check_if_rows_are_filled(empty_board):
    # empty_board.grid = [['Q', 'Q', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
    #                     ['Q', 'Q', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'],
    #                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    #                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    #                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    #                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    #                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    #                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    #                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    #                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    empty_board.add_shape(I, 2)
    empty_board.add_shape(I, 2)
    empty_board.add_shape(I, 6)
    empty_board.add_shape(I, 6)
    empty_board.add_shape(Q, 0)

    empty_board._check_if_rows_are_filled(2)
    assert empty_board.grid == [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    assert empty_board.current_height == 0
    assert empty_board.height_array == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_tetris_engine_end_to_end(empty_board):
    output_file_name = 'output_files/' + str(datetime.now()) + '_output.txt'
    tetris_engine("input_for_test.txt", output_file_name)

    # Perform assertions on the output
    expected_output = """
               Input is: I0,I4,Q8
 
               Remaining Height is: 1
               Board is: 
               ##########
##########
##########
##########
##########
##########
##########
##########
########QQ
##########
               ---- """
    output_file = get_info_in_file(output_file_name)
    assert output_file == expected_output
