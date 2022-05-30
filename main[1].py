############### Blackjack Project #####################


import random
from replit import clear

blackjack_over = False

while not blackjack_over:
  from art import logo
  
  print(logo)
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  #deals a random card
  def deal_card():
    card = random.choice(cards)
    return card
    
  player_cards = []
  computer_cards = []
  game_over = False 
  
  #each user will begin by having 2 cards. These 2 cards will be assinged randomly
  for card in range(0,2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  #calculating the total of both the opponent and the player 
  def calculate_score(cards):
    """Takes the corresponding numbers and calculates the total score"""
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    elif 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards) 
  

  #creating a while loop, where it provides the user the option to keep drawing or maintain his cards
  while not game_over:
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    print(f" The player cards are {player_cards} and your current score is {player_score}")
    print(f" The computer cards are {computer_cards} and their current score is {computer_score}" )
  
    if player_score == 0 or computer_score == 0 or player_score > 21: 
      game_over = True
    else:
      draw_again = input("\nWould you like to draw another card? Please type in 'yes' or 'no'\n")
      if draw_again == "yes":
        player_cards.append(deal_card())
      else:
        game_over = True
        
  #creating a while loop for the computer, where has to keep drawing till his over 17
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score= calculate_score(computer_cards)

  #comparing both the player's score and the computer's score 
  def compare(player, computer):
    if player == computer:
      print('Draw')
    elif computer == 0:
      print("Computer Wins. Better Luck Next Time :(")
    elif player == 0:
      print("Congratulations! You Win :D")
    elif player > 21:
      print("Oh no, you went over 21. You Lose :(")
    elif computer > 21:
      print("Congratulations! You Win :D")
    elif player > computer:
      print("Congratulations! You Win :D")
    else:
      print("You Lose. The computer has a higher score. Better Luck Next Time :(.")
  
      
      
  
  compare(player=player_score, computer=computer_score)
  
  again = input("Would you like to play again?\n")
  if again == "yes":
    clear()
  else:
    print("Goodbye. Hope you had fun :D")
    blackjack_over = True

