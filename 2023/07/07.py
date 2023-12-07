import sys
from functools import cmp_to_key

EXAMPLE_DATA = """
""".strip()

card_types_p1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_types_p2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def rank_hand_p1(hand):
    # Five of a kind, Four of a kind, Three of a kind, Two pair, One pair, High card
    ranking = [False, False, False, False, False]

    my_dict = {}

    for char in hand:
        if my_dict.get(char) is None:
            my_dict[char] = 0

        my_dict[char] += 1

    one_pair_found = False

    for el in my_dict:
        if my_dict[el] == 5:
            ranking[0] = True

        if my_dict[el] == 4:
            ranking[1] = True

        if my_dict[el] == 3:
            ranking[2] = True

        if my_dict[el] == 2:
            if one_pair_found:
                ranking[3] = True
            else:
                one_pair_found = True

    if ranking[3] == False and one_pair_found:
        ranking[4] = True

    return ranking


def rank_hand_p2(hand):
    # Five of a kind, Four of a kind, Three of a kind, Two pair, One pair, High card
    ranking = [False, False, False, False, False]

    jokers = 0
    my_dict = {}

    for char in hand:
        if char == "J":
            jokers += 1
            continue

        if my_dict.get(char) is None:
            my_dict[char] = 0

        my_dict[char] += 1

    sorted_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    my_dict = dict(sorted_list)

    if jokers == 5:
        my_dict["A"] = 5
    elif jokers:
        first_key = list(my_dict.keys())[0]
        my_dict[first_key] += jokers

    one_pair_found = False

    for el in my_dict:
        if my_dict[el] == 5:
            ranking[0] = True

        if my_dict[el] == 4:
            ranking[1] = True

        if my_dict[el] == 3:
            ranking[2] = True

        if my_dict[el] == 2:
            if one_pair_found:
                ranking[3] = True
            else:
                one_pair_found = True

    if ranking[3] == False and one_pair_found:
        ranking[4] = True

    return ranking


def custom_compare_p1(item1, item2):
    x1, bid1, _ = item1
    x2, bid2, _ = item2

    for i in range(5):
        if x1[i] == True and x2[i] == False:
            return -1

        if x1[i] == False and x2[i] == True:
            return 1

    for i in range(len(bid1)):
        c1 = str(bid1[i])
        c2 = str(bid2[i])

        if card_types_p1.index(c1) > card_types_p1.index(c2):
            return 1

        if card_types_p1.index(c1) < card_types_p1.index(c2):
            return -1

    return 0


def custom_compare_p2(item1, item2):
    x1, bid1, _ = item1
    x2, bid2, _ = item2

    for i in range(5):
        if x1[i] == True and x2[i] == False:
            return -1

        if x1[i] == False and x2[i] == True:
            return 1

    for i in range(len(bid1)):
        c1 = str(bid1[i])
        c2 = str(bid2[i])

        if card_types_p2.index(c1) > card_types_p2.index(c2):
            return 1

        if card_types_p2.index(c1) < card_types_p2.index(c2):
            return -1

    return 0


def main():
    answer1 = 0
    answer2 = 0

    data = (
        open(sys.argv[2], "r").read()
        if len(sys.argv) > 2 and sys.argv[1] == "--data"
        else EXAMPLE_DATA
    )

    lines = list(filter(None, data.split("\n")))

    cards_p1 = []
    cards_p2 = []

    for line in lines:
        hand, value = line.split()
        ranked_hand_p1 = rank_hand_p1(hand)
        ranked_hand_p2 = rank_hand_p2(hand)
        cards_p1.append((ranked_hand_p1, hand, value))
        cards_p2.append((ranked_hand_p2, hand, value))

    sorted_cards_p1 = sorted(cards_p1, key=cmp_to_key(custom_compare_p1), reverse=True)
    sorted_cards_p2 = sorted(cards_p2, key=cmp_to_key(custom_compare_p2), reverse=True)

    for i, card in enumerate(sorted_cards_p1):
        value = int(card[2])
        answer1 += (i + 1) * value

    for i, card in enumerate(sorted_cards_p2):
        value = int(card[2])
        answer2 += (i + 1) * value

    print("Answer 1: ", answer1)
    print("Answer 2: ", answer2)


if __name__ == "__main__":
    main()
