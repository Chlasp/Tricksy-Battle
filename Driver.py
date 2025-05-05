import random
from logic_func import *

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
player_cards = deck[:8]
computer_cards = deck[8:16]

# Deck remainder
deck_remainder = deck[16:]

# Initializing player scored
player_score = 0
computer_score = 0

# Initializing current round and leading player
current_round = 1
leading_player = random.choice([1, 2]) # random player leads first

# Get number of rounds player wants to play
while True:
    try:
        max_rounds = int(input("Please input the number of rounds you want to play(even numbers only between 2 and 16): "))
        if max_rounds % 2 == 0 and 2 <= max_rounds <= 16:
            break
        else:
            print("Please enter an even number between 2 and 16.")
    except ValueError:
        print("Please enter a valid number.")
# Game loop
while current_round <= max_rounds:
    # Display current round
    print(f"Round {current_round}")

    # Display leading player
    print(f"Leading player: ", "You" if leading_player == 1 else "Computer")

    # Display player cards
    print(f"Player's cards: {player_cards}")
    if leading_player == 1:
        while True:
            decision = input("Choose a card to play (Input is case sensitive): ").strip()
            if decision.lower() == "quit": # allows player to wuit the game whenever they want
                print("You quit the game.")
                break
            rank, _,suit = decision.partition(' of ')
            player_card = (rank, suit)
            if player_card in player_cards:
                player_cards.remove(player_card) # removes card from player's hand 
                break
            print("Invalid card. Please choose a card from your hand.")
        
        # Computer's turn if player is leading
        lead_suit = player_card[1]
        computer_card = follow_suit(computer_cards, lead_suit)
        computer_cards.remove(computer_card) ## removes card from computer's hand
    else:
        # If computer is leading
        computer_card = random.choice(computer_cards)
        lead_suit = computer_card[1]
        print(f"Computer leads with {computer_card[0]} of {computer_card[1]}")
        
        # Player's turn if computer is leading
        valid_cards = [card for card in player_cards if card[1] == lead_suit]
        while True:
            decision = input("Choose a card to play (Input is case sensitive): ").strip()
            rank, _,suit = decision.partition(' of ')
            player_card = (rank, suit)
            if player_card not in player_cards:
                print("Invalid card. Please choose a card from your hand.")
                continue
                
            if valid_cards and player_card not in valid_cards:
                    print(f"Invalid card. You must follow suit. {lead_suit}")
                    continue
            player_cards.remove(player_card) # removes card from player's hand
            break
                
    print(f"You play {player_card[0]} of {player_card[1]}")
    print(f"Computer plays {computer_card[0]} of {computer_card[1]}")
    
    # To determine winner
    winner = play(player_card, computer_card, lead_suit)
    if winner == "Player":
        player_score += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        leading_player = 1 # player leads next round
    else:
        computer_score += 1
        leading_player = 2  # computer leads next round
    
    # Reveal and discard card from deck
    if deck_remainder:
        removed_card = deck_remainder.pop()
        print(f"Revealed and discarded card: {removed_card[0]} of {removed_card[1]}")
        
    # Re-deal 4 cards when player and computer have 4 cards left
    if len(player_cards) == 4 and len(deck_remainder) >= 8:
        print("Re-dealing 4 cards to each player")
        player_cards += deck_remainder[:4]
        computer_cards += deck_remainder[4:8]
        deck_remainder = deck_remainder[8:]
    
    # Increment current round
    current_round += 1
    
# Decide winner and display scores
print("Game over")
if player_score == 0 and computer_score == 16:
    print("You shot the moon!, You win with 17 points!")
elif computer_score == 0 and player_score == 16:
    print("Computer shot the moon!, Computer wins with 17 points!")
elif player_score > computer_score:
    print(f"You win with {player_score} points!, Computer: {computer_score} points")
elif computer_score > player_score:
    print(f"Computer wins with {computer_score} points!, You: {player_score} points")
else:
    print("It's a tie!")
        