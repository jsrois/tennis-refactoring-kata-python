# -*- coding: utf-8 -*-

class TennisGame1:
    def __init__(self, player1, player2):
        self.player_scores = {
            player1: 0,
            player2: 0
        }

    def won_point(self, player):
        self.player_scores[player] += 1

    def players_have_the_same_points(self):
        scores = self.player_scores.values()
        return scores[0] == scores[1]

    def score(self):
        result = ""
        temp_score = 0
        if self.players_have_the_same_points():
            return self.tied_score()

        player1, player2 = sorted(self.player_scores.items())

        if (player1[1] >= 4 or player2[1] >= 4):
            minusResult = player1[1] - player2[1]
            if (minusResult == 1):
                result = "Advantage " + player1[0]
            elif (minusResult == -1):
                result = "Advantage " + player2[0]
            elif (minusResult >= 2):
                result = "Win for " + player1[0]
            else:
                result = "Win for " + player2[0]
            return result

        for i in range(1, 3):
            if (i == 1):
                temp_score = player1[1]
            else:
                result += "-"
                temp_score = player2[1]
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[temp_score]
        return result

    def tied_score(self):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.player_scores.values()[0], "Deuce")
