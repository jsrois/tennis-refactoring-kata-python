FORTY  = 3


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def won_point(self):
        self.score += 1

    def advantage_over(self, player):
        return self.score - player.score


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

        winning_player, losing_player = self.whos_winning()

        if winning_player.score > FORTY:
            if winning_player.advantage_over(losing_player) > 1:
                return self.winning_result(winning_player)
            return self.advantage_for(winning_player)

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

    def whos_winning(self):
        return sorted(self.players, key=lambda player: player.score, reverse=True)

    def winning_result(self, winning_player):
        return "Win for " + winning_player.name

    def advantage_for(self, winning_player):
        return "Advantage " + winning_player.name
