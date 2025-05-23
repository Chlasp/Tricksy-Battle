import random

rank_values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12}

def get_card_value(card): # get the nuremical value of a card
    rank, suit = card
    return rank_values[rank]

def follow_suit(hand, suit): # check if a player has a card of a certain suit
    cards_of_same_suit = [card for card in hand if card[1] == suit]
    if cards_of_same_suit:
        return random.choice(cards_of_same_suit)
    return random.choice(hand)

def play(card1, card2, lead_suit):
    if card1[1] == lead_suit and card2[1] != lead_suit:
        return "Player"
    if card2[1] == lead_suit and card1[1] != lead_suit:
        return "Computer"
    return "Player" if get_card_value(card1) > get_card_value(card2) else "Computer"