import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # 注意下面这两种情况的区别
        # self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(deck._cards)
print(len(deck))
print(deck[0])
print(deck[-1])
# 随机从序列中选取一个元素
print(choice(deck))
print(choice(deck))
# 取前三个元素
print(deck[:3])
# 取包含A的元素
print(deck[12::13])
# 为什么后面会是False呢？
print(type(deck), isinstance(deck, list), isinstance(deck, collections.Iterable))
# 实现了__getitem__方法，deck就变成可迭代的了
for card in deck:
    print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
