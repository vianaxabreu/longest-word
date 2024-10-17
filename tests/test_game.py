import string
from longest_word.game import Game


class TestGame:
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        new_game = Game()
        assert new_game.is_valid("") is False

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list("KWEUEAKRZ")  # Force the grid to a test case:
        assert new_game.is_valid("EUREKA") is True
        assert new_game.grid == list(
            "KWEUEAKRZ"
        )  # Make sure the grid remained untouched

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list("KWEUEAKRZ")  # Force the grid to a test case:
        assert new_game.is_valid("SANDWICH") is False
        assert new_game.grid == list(
            "KWEUEAKRZ"
        )  # Make sure the grid remained untouched
