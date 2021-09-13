from collections import deque


def the_biggest(cards: list, max_number: int):
    sort = sorted(cards)
    if max_number in cards and 1 in cards:
        return cards.index(1)
    return cards.index(sort[-1])


def game_of_pigs(count: int, players: int, cards: list):
    reversed_cards = list(reversed(cards))
    pigs = []
    for i in range(1, players+1):
        pigs.append(deque(reversed_cards[players-i::players]))

    while True:
        amount = []
        for i in range(players):
            if pigs[i]:
                amount.append(pigs[i].popleft())
            else:
                amount.append(0)

        member = the_biggest(amount, count)
        clean_cards = [i for i in amount if i != 0]

        if len(clean_cards) <= 1:
            return pigs
        pigs[member].extend(clean_cards)


if __name__ == '__main__':
    n = int(input())
    cards_in = list(map(int, input().split()))
    winner = game_of_pigs(n, 3, cards_in)
    for v, k in enumerate(winner, start=1):
        if k:
            print(v)
