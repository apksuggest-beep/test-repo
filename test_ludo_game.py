import unittest

from ludo_game import LudoGame


class LudoGameTests(unittest.TestCase):
    def test_game_starts_with_all_players_at_zero(self) -> None:
        game = LudoGame(["A", "B"])
        self.assertEqual(game.positions, {"A": 0, "B": 0})

    def test_move_advances_player_position(self) -> None:
        game = LudoGame(["A", "B"], board_size=10)
        position = game.move("A", 4)
        self.assertEqual(position, 4)
        self.assertEqual(game.positions["A"], 4)

    def test_move_caps_at_board_size_and_sets_winner(self) -> None:
        game = LudoGame(["A", "B"], board_size=10)
        game.move("A", 9)
        position = game.move("A", 6)
        self.assertEqual(position, 10)
        self.assertEqual(game.winner, "A")

    def test_play_turn_rotates_current_player(self) -> None:
        game = LudoGame(["A", "B"])
        player, roll, _ = game.play_turn(steps=3)
        self.assertEqual(player, "A")
        self.assertEqual(roll, 3)
        self.assertEqual(game.current_player(), "B")


if __name__ == "__main__":
    unittest.main()
