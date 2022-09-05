import Art
import random
import os


game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ")
if game =="y":
    os.system ('cls')
    print (Art.logo)
    def deal_cards():
        cards = [11, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card
    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    def compare(user_score,pc_score):
        if user_score == pc_score:
            return "Draw"
        elif pc_score == 0:
            return "Lose, opponent has Blackjack!"
        elif user_score == 0:
            return "Win with a Blackjack! "
        elif user_score > 21:
            return "You went over. You lose"
        elif pc_score > 21:
            return "Opponent went over. You win."
        elif user_score > pc_score:
            return "You win."
        else:
            return "You lose."

        
    user_cards=[]
    pc_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        pc_cards.append(deal_cards())

    
    while not is_game_over:
        user_score  = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)

        print (f"Your cards: {user_cards}, current score: {user_score} ")
        print (f"Computer's first card: {pc_cards[0]}")

        if user_score == 0 or pc_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ") 
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True
    
    while pc_score != 0 and pc_score < 17:
        pc_cards.append(deal_cards())
        pc_score = calculate_score(pc_cards)
    
    print (f" Your final hand: {user_cards}, final score: {user_score}")
    print (f" Opponent's final hand: {pc_cards}, final score: {pc_score}")
    print (compare(user_score,pc_score))

        



