import unittest
import copy
from unittest.mock import patch
from run import (show_board, create_ship, get_board_coordinates,
                 count_hits, reset_game_state, BOARD_SIZES_DICT)


class TestBattleships(unittest.TestCase):

    # G-TEST-1: Verifies show_board function does not raise any unexpected exception.
    def test_show_board(self):
        board = [[" " for _ in range(4)] for _ in range(4)]
        try:
            show_board(board)
        except (TypeError, ValueError, IndexError, IOError, UnicodeEncodeError) as e:
            self.fail(f"Unexpected exception: {e}")

    # G-TEST-2: Checks if create_ship function places 5 ships on the board.
    def test_create_ship(self):
        board = [[" " for _ in range(4)] for _ in range(4)]
        create_ship(board)
        ship_count = sum(1 for row in board for cell in row if cell == "S")
        self.assertEqual(ship_count, 5)

    # G-TEST-3: Validates get_board_coordinates function 
    # returns correct coordinates for valid input.
    def test_get_board_coordinates_valid(self):
        with patch('builtins.input', side_effect=["1", "A"]):
            result = get_board_coordinates([[" " for _ in range(4)] for _ in range(4)])
            expected_result = (0, 0)
            self.assertEqual(result, expected_result)

    # G-TEST-4: Tests if count_hits function returns 0 for an empty board
    def test_count_hits_empty_board(self):
        board = [[" " for _ in range(4)] for _ in range(4)]
        result = count_hits(board)
        expected_result = 0
        self.assertEqual(result, expected_result)

    # G-TEST-5: Ensures create_ship function places 5 ships on a small board.
    def test_create_ship_small_board(self):
        hidden_board = [[" " for _ in range(4)] for _ in range(4)]
        hidden_board_copy = copy.deepcopy(hidden_board)
        create_ship(hidden_board_copy)
        ship_count = sum(row.count("S") for row in hidden_board_copy)
        self.assertEqual(ship_count, 5)

    # G-TEST-6: Confirms reset_game_state function 
    # initializes small board state correctly.
    def test_reset_game_state_small_board(self):
        hidden_board, guess_board, turns_left, hit_count = reset_game_state("s")
        self.assertEqual(len(hidden_board), 4)
        self.assertEqual(len(guess_board), 4)
        self.assertEqual(turns_left, 10)
        self.assertEqual(hit_count, 0)

    # G-TEST-7: Validates reset_game_state function 
    # initializes medium board state correctly.
    def test_reset_game_state_medium_board(self):
        hidden_board, guess_board, turns_left, hit_count = reset_game_state("m")
        self.assertEqual(len(hidden_board), 6)
        self.assertEqual(len(guess_board), 6)
        self.assertEqual(turns_left, 10)
        self.assertEqual(hit_count, 0)

    # G-TEST-8: Verifies reset_game_state function 
    # initializes large board state correctly.
    def test_reset_game_state_large_board(self):
        hidden_board, guess_board, turns_left, hit_count = reset_game_state("l")
        self.assertEqual(len(hidden_board), 8)
        self.assertEqual(len(guess_board), 8)
        self.assertEqual(turns_left, 10)
        self.assertEqual(hit_count, 0)

    # G-TEST-9: Checks if BOARD_SIZES_DICT has the correct keys.
    def test_board_size_dict_correct_keys(self):
        self.assertTrue(set(BOARD_SIZES_DICT.keys()) == {"s", "m", "l"})

    # G-TEST-10: Asserts reset_game_state function 
    # raises a ValueError for an invalid board size.
    def test_reset_game_state_invalid_board_size(self):
        with self.assertRaises(ValueError):
            reset_game_state("invalid_board_size")


if __name__ == "__main__":
    unittest.main()
