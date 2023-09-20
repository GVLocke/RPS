import random
import time
import numpy as np

random.seed(time.time())


class RPS:
    def __init__(self, count, players):
        self.__count = count
        self.__ties = 1
        self.__wins = count - 1
        self.__losses = count - 1
        # The below code makes it so that the first three players are always Rock, Paper, and Scissors. It only
        # works if the number of players is greater than or equal to 3.
        # self.__player_list = ["Rock", "Paper", "Scissors"]
        # for i in range(count - 3):
        #     self.__player_list.append(random.choice(RPS.players))
        self.__player_list = players
        self.__win_matrix = np.zeros((count, count), dtype=int)
        for i in range(count):
            for j in range(count):
                if i == j:
                    self.__win_matrix[i, j] = 0
                elif (i < j and (i % 2 == 0 and j % 2 == 0)) or (i < j and (i % 2 == 1 and j % 2 == 1)):
                    self.__win_matrix[i, j] = 1
                elif (i > j and (i % 2 == 1 and j % 2 == 0)) or (i > j and (i % 2 == 0 and j % 2 == 1)):
                    self.__win_matrix[i, j] = 1

    def get_count(self):
        return self.__count

    def get_ties(self):
        return self.__ties

    def get_wins(self):
        return self.__wins

    def get_losses(self):
        return self.__losses

    def get_player_list(self):
        return self.__player_list

    def randomize_player_list(self):
        random.shuffle(self.__player_list)

    def get_win_matrix(self):
        return self.__win_matrix

    def print_results(self):
        for i in range(self.__count):
            for j in range(self.__count):
                if self.__win_matrix[i, j] == 1:
                    print(f"{self.__player_list[i]} beats {self.__player_list[j]}")

    def play_game(self):
        print("Welcome Player 1!".center(40, "-"))
        print(f"There are {self.get_count()} options.")
        for i in range(self.get_count()):
            print(f"{i + 1}. {self.get_player_list()[i]}")
        while 1:
            player_one_selection_option = str(input("Enter your selection: "))
            if not player_one_selection_option.isdigit():
                print(f"Please choose a number between 1 and {self.get_count()}.")
                continue
            elif int(player_one_selection_option) < 1 or int(player_one_selection_option) > self.get_count():
                print(f"Please choose a number between 1 and {self.get_count()}.")
                continue
            else:
                player_one_selection = int(player_one_selection_option)
                break
        # clear the screen
        print("\033[H\033[J", end="")
        print("Welcome Player 2!".center(40, "-"))
        print(f"There are {self.get_count()} options.")
        for i in range(self.get_count()):
            print(f"{i + 1}. {self.get_player_list()[i]}")
        while 1:
            player_two_selection_option = str(input("Enter your selection: "))
            if not player_two_selection_option.isdigit():
                print(f"Please choose a number between 1 and {self.get_count()}.")
                continue
            elif int(player_two_selection_option) < 1 or int(player_two_selection_option) > self.get_count():
                print(f"Please choose a number between 1 and {self.get_count()}.")
                continue
            else:
                player_two_selection = int(player_two_selection_option)
                break
        # clear the console
        print("\033[H\033[J", end="")
        print("Results".center(40, "-"))
        print(f"Player 1: {self.get_player_list()[player_one_selection - 1]}")
        print(f"Player 2: {self.get_player_list()[player_two_selection - 1]}")
        if self.get_win_matrix()[player_one_selection - 1, player_two_selection - 1] == 1:
            print("Player 1 wins!")
        elif player_two_selection == player_one_selection:
            print("It's a tie!")
        else:
            print("Player 2 wins!")


if __name__ == "__main__":
    # get the number of players
    while 1:
        count_option = str(input("How many players? "))
        if not count_option.isdigit():
            print("Please enter a number.")
            continue
        elif int(count_option) < 2:
            print("Please enter a number greater than 1.")
            continue
        else:
            count = int(count_option)
            break
    # get the player names
    players = []
    for i in range(count):
        players.append(str(input("Enter a player name: ")))
    # create the game
    game = RPS(count, players)
    # print the results
    game.print_results()
    print(game.get_win_matrix())
