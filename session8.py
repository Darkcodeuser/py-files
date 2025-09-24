import random

### Card suits and ranks

SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
RANK_VALUE = {r: i for i, r in enumerate(RANKS, start=2)}  # 2 -> 2, ..., A -> 14

def make_deck():
    return [(r, s) for s in SUITS for r in RANKS]

def card_str(card):
    return f"{card[0]} of {card[1]}"

def print_hand(hand):
    print(", ".join(card_str(c) for c in hand))

def sort_hand(hand):
    return sorted(hand, key=lambda c: (SUITS.index(c[1]), RANK_VALUE[c[0]]))

def valid_moves(hand, lead_suit):
    if lead_suit is None:
        return hand[:]
    same = [c for c in hand if c[1] == lead_suit]
    return same if same else hand[:]

def pick_card_ai(hand, lead_suit):
    moves = valid_moves(hand, lead_suit)
    return min(moves, key=lambda c: (c[1] != lead_suit, RANK_VALUE[c[0]]))

def trick_winner(lead_suit, trick_cards, trump):
    trump_cards = [(p, c) for p, c in trick_cards if c[1] == trump]
    if trump_cards:
        winner = max(trump_cards, key=lambda pc: RANK_VALUE[pc[1][0]])
        return winner[0]
    lead_cards = [(p, c) for p, c in trick_cards if c[1] == lead_suit]
    winner = max(lead_cards, key=lambda pc: RANK_VALUE[pc[1][0]])
    return winner[0]

def play_round():
    deck = make_deck()
    random.shuffle(deck)

  ###cards
    hands = [sorted(deck[i*13:(i+1)*13], key=lambda c: (SUITS.index(c[1]), RANK_VALUE[c[0]])) for i in range(4)]

 
    trump = random.choice(SUITS)
    print(f"Trump suit: {trump}")

    scores = [0,0,0,0]
    leader = 0  

    for trick_index in range(13):
        print("\n" + "="*20)
        print(f"Trick {trick_index+1}, leader: Player {leader}")
        trick_cards = []
        lead_suit = None

        for i in range(4):
            player = (leader + i) % 4
            hand = hands[player]

            if player == 0:
                ###player

                print("\nYour hand:")
                print_hand(sort_hand(hand))
                moves = valid_moves(hand, lead_suit)
                print("Playable cards:")
                for idx, c in enumerate(moves):
                    print(f"{idx+1}. {card_str(c)}")
                while True:
                    choice = input(f"Choose a number (1-{len(moves)}): ").strip()
                    if not choice.isdigit():
                        print("Please enter a number.")
                        continue
                    choice = int(choice)
                    if 1 <= choice <= len(moves):
                        card = moves[choice-1]
                        break
                    else:
                        print("Out of range.")
            else:
                ###bot

                card = pick_card_ai(hand, lead_suit)

            hand.remove(card)
            trick_cards.append((player, card))
            if lead_suit is None:
                lead_suit = card[1]
            print(f"Player {player} plays {card_str(card)}")

        ###trick winner

        winner = trick_winner(lead_suit, trick_cards, trump)
        print(f"Trick winner: Player {winner}")
        scores[winner] += 1
        leader = winner

    print("\n" + "="*30)
    print("Final results (tricks won):")
    for p in range(4):
        print(f"Player {p}: {scores[p]}")

if __name__ == "__main__":
    print("Simple Hokm game - 4 players. You are Player 0.")
    play_round()
