import random

# list of card names and ranks
suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen"]

# Comparison for rank to values
rank_values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12}

# 1. Create a deck of cards
deck = [(rank, suit) for suit in suits for rank in ranks]

# Shuffle deck
random.shuffle(deck)

# Deal 8 cards to each player
player1_cards = deck[:8]
player2_cards = deck[8:16]

# Deck remainder
deck_remainder = deck[16:]

# Initializing player scored
player1_score = 0
player2_score = 0

# Initializing current round and leading player
current_round = 1
winning_player = random.choice([1, 2]) # random player leads first