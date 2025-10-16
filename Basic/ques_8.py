# Calcuate the number of tie games & total points of games where for win points is 4 and for tie the p[oint is 2.

game_played = int(input("Enter the number of game played:" ))
game_win = int(input("Enter the number of game win:" ))
game_lost = int(input("Enter the number of game lost:" ))

total_tie_games = game_played - game_win - game_lost
print(f"Games tied = {total_tie_games}")

total_points = (game_win * 4) + (game_lost * 2)
print(f"the total points will be {total_points}")