# -*- coding: utf-8 -*-

class TennisGame1:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def players_have_the_same_points(self):
        return self.p1points == self.p2points

    def score(self):
        result = ""
        temp_score = 0
        if self.players_have_the_same_points():
            return self.tied_score()

        if (self.p1points >= 4 or self.p2points >= 4):
            minusResult = self.p1points - self.p2points
            if (minusResult == 1):
                result = "Advantage " + self.player1Name
            elif (minusResult == -1):
                result = "Advantage " + self.player2Name
            elif (minusResult >= 2):
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
            return result

        for i in range(1, 3):
            if (i == 1):
                temp_score = self.p1points
            else:
                result += "-"
                temp_score = self.p2points
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
        }.get(self.p1points, "Deuce")
