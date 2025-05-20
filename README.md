TRICKSY BATTLE - CARD GAME<br /> Overview <br /> Tricksy Battle is a simple card game implemented in Python that involves two players
(Player vs. Computer). Players take turns playing cards from their hand, following suit when possible. 
The highest card in the lead suit wins the round. After a set number of rounds, the player with the highest points wins.

<br /> GAME RULES <br />
- Standard deck of 48 cards with all Kings removed<br />
- Players are dealt 8 cards each<br />
- Other player must follow lead suit if possible<br />
- Higher-ranking cards win rounds<br />
- If players are down to 4 cards at the end of a round, they are dealt 4 more<br />
- The game goes on until the set number of rounds is met(between 2 and 16, only even numbers)<br />
- If one player scored 16 and the other scored 0, they "shoot the moon" and win with 17 points.

<br />HOW TO RUN<br />
- Make sure Python 3 is installed on your system<br />
- Place both the "Driver.py (main)" and "logic_func.py" files in the same directory<br />

<br />RUNNING THE GAME<br />
- Open terminal and navigate to the folder containing the game files, then press the run button<br />
- It can also be run in the command prompt using Python interpreter, for example," python Driver.py"

<br />HOW TO PLAY<br />
- When prompted, enter the number of rounds (an even number between 2 and 16)<br />
- The game will then display your hand and who is leading each round (Player or Computer)<br />
- Type in the card you want to play (Input is case sensitive, for example, "5 of Hearts" not "5 of hearts")<br />
- If you are following suit and you have a matching card, you must play it<br />
- After the final round, the score and winner are displayed<br />
- You can also quit the game anytime by typing "quit"<br />

<br /> ADDITIONAL FEATURES <br />
- Time tracking <br />- The game tracks how long each round takes, and the cumulative time is displayed at the end
- Score progress Graph <br /> - After the game ends, a line graph shows the progress of the player's score across rounds
