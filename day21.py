def read_data ():
    with open("dayXX.txt", "r") as f:
        pass


class DetermDie (object):
    def __init__(self):
        self.n = 1
        self.count = 0

    def roll(self):
        v = self.n
        self.n = (self.n % 100) + 1
        self.count += 1
        return v


class Player (object):
    def __init__(self, n, pos):
        self.n = n
        self.pos = pos
        self.score = 0

    def turn (self, die):
        roll = die.roll() + die.roll() + die.roll()
        self.pos = (self.pos + roll - 1) % 10 + 1
        self.score += self.pos
        print ("player {} rolls {}, is at {}, score is now {}".format(self.n, roll, self.pos, self.score))


def day1 (pos1, pos2):
    players = [Player(1, pos1), Player(2, pos2)]
    die = DetermDie()
    p = 0
    while players[0].score < 1000 and players[1].score < 1000:
        players[p].turn(die)
        p = (p+1)%2

    print (players[p].score, die.count, players[p].score * die.count)


def gen_dirac():
    outcomes = {}
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i+j+k+3) in outcomes:
                    outcomes[i+j+k+3] += 1
                else:
                    outcomes[i+j+k+3] = 1
    return outcomes

def day2(pos1, pos2):
    states = {}
    dirac_die = gen_dirac()
    universes = {(pos1, pos2, 0, 0, 0): 1}
    wins = {1:0, 2:0}
    for state, ucount in universes.items():
        pos1, pos2, score1, score2, player = state
        for roll, count in dirac_die.items():
            if player == 0:
                pos1 = (pos1 + roll - 1) % 10 + 1
                score1 += pos1
            else:
                pos2 = (pos2 + roll - 1) % 10 + 1
                score2 += pos2
            if score1 > 21 or score2 > 21:
                wins[1 if score1 > 21 else 2] += count * ucount
            else:
                universes[(pos1, pos2, score1, score2, 1 if player == 0 else 0)] = count * ucount
        del universes[state]
        print (len(universes.keys()), sum(universes.values()))





if __name__ == "__main__":
    pos = (4, 8)
    # pos = (6, 4)
    day1 (*pos)
    day2 (*pos)
