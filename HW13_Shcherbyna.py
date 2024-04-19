class SingleplayerMeta(type):
    _players = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._players:
            player = super().__call__(*args, **kwargs)
            cls._players[cls] = player
        return cls._players[cls]


class Singleplayer(metaclass=SingleplayerMeta):
    def __init__(self, player_name: str, game_difficulty: str):
        self.player_name = player_name
        self.game_difficulty = game_difficulty

    def print_game_report(self):
        print(f"Player {self.player_name} is playing in solo mode on {self.game_difficulty} difficulty.")


# Use example
player1 = Singleplayer("Bob", "Easy")
player2 = Singleplayer("Rob", "Extreme")

player1.print_game_report()
player2.print_game_report()

if id(player1) == id(player2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")
