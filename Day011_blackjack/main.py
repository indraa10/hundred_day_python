import random as r


def deal_card():
    """ return a random card from the deck """
    cards = {'ace': [1, 11], 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
             'ten': 10, 'jack': 10, 'queen': 10, 'king': 10}
    card_selected = r.choice(list(cards.keys()))

    if card_selected == 'ace':
        return r.choice(cards[card_selected])
    else:
        return cards[card_selected]


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "you lose, opponent has blackjack "
    elif user_score == 0:
        return "you win with a blackjack"
    elif user_score > 21:
        return "you went over , you lose"
    elif computer_score > 21:
        return "opponent went over. you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you loose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" your cards: {user_cards}, current score: {user_score}")
        # print(f" Computer's first card: {computer_cards}, current score: {computer_score}")
        print(f" Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand : {user_cards}, final score: {user_score}")
    print(f" Computer's final hand : {computer_cards},final score : {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n' : ") == "y":
    play_game()
