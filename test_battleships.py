import unittest
import copy
from unittest.mock import patch
from run import (show_board, create_ship, get_board_coordinates,
                 count_hits, reset_game_state, BOARD_SIZES_DICT)


class TestBattleships(unittest.TestCase):

    # TEST-1: Verifies that the show_board function
    # does not raise any unexpected exception.
    def test_show_board(self):
        board = [[" " for _ in range(4)] for _ in range(4)]
        try:
            show_board(board)
        except (TypeError, ValueError, IndexError,
                IOError, UnicodeEncodeError) as e:
            self.fail(f"Unexpected exception: {e}")

    # TEST-2: Checks if the create_ship function places 5 ships on the board.
    def test_create_ship(self):
        board = [[" " for _ in range(4)] for _ in range(4)]
        create_ship(board)
        ship_count = sum(1 for row in board for cell in row if cell == "S")
        self.assertEqual(ship_count, 5)

    # TEST-3: Validates that the get_board_coordinates function
    # returns correct coordinates for valid input.
    def test_get_board_coordinates_valid(self):
        with patch('builtins.input', side_effect=["1", "A"]):
            result = get_board_coordinates(
                [[" " for _ in range(4)] for _ in range(4)])
            expected_result = (0, 0)
            self.assertEqual(result, expected_result)

    # TEST-4: Tests if the count_hits function returns 0 for an empty board
    def test_count_hits_empty_board(self):
        board = [[" " for _ in range(4)] for _ in range(4)]
        result = count_hits(board)
        expected_result = 0
        self.assertEqual(result, expected_result)

    # TEST-5: Ensures that the create_ship function
    # places 5 ships on a small board.
    def test_create_ship_small_board(self):
        hidden_board = [[" " for _ in range(4)] for _ in range(4)]
        hidden_board_copy = copy.deepcopy(hidden_board)
        create_ship(hidden_board_copy)
        ship_count = sum(row.count("S") for row in hidden_board_copy)
        self.assertEqual(ship_count, 5)

    # TEST-6: Confirms that the reset_game_state function
    # initializes small board state correctly.
    def test_reset_game_state_small_board(self):
        game_state = reset_game_state("s")
        hidden_board, guess_board, turns_left, hit_count = game_state
        self.assertEqual(len(hidden_board), 4)
        self.assertEqual(len(guess_board), 4)
        self.assertEqual(turns_left, 10)
        self.assertEqual(hit_count, 0)

    # TEST-7: Validates that the reset_game_state function
    # initializes medium board state correctly.
    def test_reset_game_state_medium_board(self):
        game_state = reset_game_state("m")
        hidden_board, guess_board, turns_left, hit_count = game_state
        self.assertEqual(len(hidden_board), 6)
        self.assertEqual(len(guess_board), 6)
        self.assertEqual(turns_left, 10)
        self.assertEqual(hit_count, 0)

    # TEST-8: Verifies that the reset_game_state function
    # initializes large board state correctly.
    def test_reset_game_state_large_board(self):
        game_state = reset_game_state("l")
        hidden_board, guess_board, turns_left, hit_count = game_state
        self.assertEqual(len(hidden_board), 8)
        self.assertEqual(len(guess_board), 8)
        self.assertEqual(turns_left, 10)
        self.assertEqual(hit_count, 0)

    # TEST-9: Checks if BOARD_SIZES_DICT has the correct keys.
    def test_board_size_dict_correct_keys(self):
        self.assertTrue(set(BOARD_SIZES_DICT.keys()) == {"s", "m", "l"})

    # TEST-10: Ensures that the reset_game_state function
    # raises a ValueError for an invalid board size.
    def test_reset_game_state_invalid_board_size(self):
        with self.assertRaises(ValueError):
            reset_game_state("invalid_board_size")


if __name__ == "__main__":
    unittest.main()
