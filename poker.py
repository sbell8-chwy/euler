
class Hand:
    def __init__(self, hand):
        self.hand = hand

    def compute_value(self):
        is_straight = self.straight()
        is_flush = self.flush()
        if is_straight and is_flush:
            return (8, self.ranks()[0])
        if self.kind(4):
            return (7, self.kind(4), self.kind(1))
        if self.kind(3) and self.kind(2):
            return (6, self.kind(3), self.kind(2))
        if is_flush:
            return (5, self.ranks())
        if is_straight:
            return (4, self.ranks()[0])
        if self.kind(3):
            return (3, self.kind(3), self.ranks())
        if self.two_pair():
            return (2, self.two_pair(), self.ranks())
        if self.kind(2):
            return (1, self.kind(2), self.ranks())
        else:
            return (0, self.ranks())

    def ranks(self):
        ranks = ['--23456789TJQKA'.index(r) for r,s in self.hand]
        ranks.sort(reverse=True)
        if ranks == [14, 5, 4, 3, 2]:
            return [5, 4, 3, 2, 1]
        return ranks

    def straight(self):
        ranks = self.ranks()
        if len(set(ranks)) == 5 and ranks[0] - ranks[4] == 4:
            return True
        return False

    def flush(self):
        if len(set([s for r,s in self.hand])) == 1:
            return True
        return False

    def kind(self, n):
        count = 1
        ranks = self.ranks()
        for i in range(len(ranks)):
            if i == (len(ranks) - 1) or ranks[i] != ranks[i + 1]:
                if count == n:
                    return ranks[i]
                count = 1
            else:
                count += 1
        return None

    def two_pair(self):
        ranks = self.ranks()
        one = None
        two = None
        for r in set(ranks):
            if ranks.count(r) == 2:
                if not one:
                    one = r
                else:
                    two = r
        if one and two:
            return (one, two)
        return None

if __name__ == "__main__":
    game = []
    f = open('poker.txt')
    for line in f:
        row = line.split()
        game.append((row[:5], row[5:]))

    one = 0
    for g in game:
        if Hand(g[0]).compute_value() > Hand(g[1]).compute_value():
            one += 1
    print one
