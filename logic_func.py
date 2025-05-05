import random

rank_values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12}

def get_card_value(card): # get the nuremical value of a card
    rank, suit = card
    return rank_values[rank]

def follow_suit(hand, suit): # check if a player has a card of a certain suit
    return any(card[1] == suit for card in hand)

def play_round(player1_cards, player2_cards, lead_player): # To simulate a round and return winner of said round
    if lead_player == 1:
        lead_card = player1_cards.pop(random.randint(0, len(player1_cards)-1)) # First player plays random card
        print("Player 1 leads with {lead_card}")
        lead_suit = lead_card[1]