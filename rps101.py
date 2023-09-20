from rps import RPS

players = [f"x{i}" for i in range(1, 102)]
game = RPS(101, players)
game.randomize_player_list()
game.play_game()
