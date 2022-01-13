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





def day2(data):
    pass


if __name__ == "__main__":
    pos = (4, 8)
    pos = (6, 4)
    day1 (*pos)
