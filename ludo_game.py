from __future__ import annotations

import random


class LudoGame:
    def __init__(self, players: list[str], board_size: int = 30) -> None:
        if len(players) < 2:
            raise ValueError("At least two players are required.")
        if board_size < 1:
            raise ValueError("Board size must be positive.")

        self.players = players
        self.board_size = board_size
        self.positions = {player: 0 for player in players}
        self.turn_index = 0
        self.winner: str | None = None

    def current_player(self) -> str:
        return self.players[self.turn_index]

    def roll_dice(self) -> int:
        return random.randint(1, 6)

    def move(self, player: str, steps: int) -> int:
        if self.winner is not None:
            raise RuntimeError("Game is already finished.")
        if player not in self.positions:
            raise ValueError("Unknown player.")
        if steps < 1:
            raise ValueError("Steps must be positive.")

        next_position = min(self.positions[player] + steps, self.board_size)
        self.positions[player] = next_position

        if next_position == self.board_size:
            self.winner = player

        return next_position

    def play_turn(self, steps: int | None = None) -> tuple[str, int, int]:
        if self.winner is not None:
            raise RuntimeError("Game is already finished.")

        player = self.current_player()
        roll = self.roll_dice() if steps is None else steps
        position = self.move(player, roll)
        self.turn_index = (self.turn_index + 1) % len(self.players)
        return player, roll, position


def _prompt_players() -> list[str]:
    names = input("Enter player names (comma-separated): ").strip()
    players = [name.strip() for name in names.split(",") if name.strip()]
    if len(players) < 2:
        raise ValueError("Please enter at least two player names.")
    return players


def main() -> None:
    print("Welcome to Ludo!")
    players = _prompt_players()
    game = LudoGame(players)

    while game.winner is None:
        player = game.current_player()
        input(f"{player}'s turn. Press Enter to roll the dice...")
        turn_player, roll, position = game.play_turn()
        print(f"{turn_player} rolled {roll} and moved to {position}/{game.board_size}.")

    print(f"\n🎉 {game.winner} wins the game!")


if __name__ == "__main__":
    main()
