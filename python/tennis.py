class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def won_point(self):
        self.score += 1


class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.players = [Player(player1_name), Player(player2_name)]

    def won_point(self, name):
        self.get_player_by(name).won_point()

    def score(self):
        result = ""
        temp_score = 0
        if self.players_have_the_same_score():
            return self.tied_result()
        if self.players[0].score >= 4 or self.players[1].score >= 4:
            minus_result = self.players[0].score - self.players[1].score
            if minus_result == 1:
                result = "Advantage " + self.players[0].name
            elif minus_result == -1:
                result = "Advantage " + self.players[1].name
            elif minus_result >= 2:
                result = "Win for " + self.players[0].name
            else:
                result = "Win for " + self.players[1].name
            return result

        for i in range(1, 3):
            if i == 1:
                temp_score = self.players[0].score
            else:
                result += "-"
                temp_score = self.players[1].score
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[temp_score]
        return result

    def tied_result(self):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.players[0].score, "Deuce")

    def players_have_the_same_score(self):
        return self.players[0].score == self.players[1].score

    def get_player_by(self, name):
        if self.players[0].name == name:
            return self.players[0]
        return self.players[1]
