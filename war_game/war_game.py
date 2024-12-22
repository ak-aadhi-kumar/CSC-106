# Copyright (C) 2024 Aadhi Kumar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random

# 1xx = Spades
# 2xx = Diamonds
# 3xx = Clubs
# 4xx = Hearts
# 5xx = Jokers
# x02-x10 = numbered cards
# x11 = Jack
# x12 = Queen
# x13 = King
# x14 = Ace

master_deck = [
    # Spades
    102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
    # Diamonds
    202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214,
    # Clubs
    302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314,
    # Hearts
    402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414,
    # Jokers, we won't include these for now
    # 501, 502
]

cpu_deck = []
cpu_win_pile = []
player_deck = []
player_win_pile = []

# NOTE: Code used for populating deck, already ran once, stored output in `master_deck` array
def create_deck():
    for i in range(100, 500, 100):
        for j in range(2, 15):
            deck.append(i+j)
    deck.append(501)
    deck.append(502)

# Shuffle that deck good so no salty looser accuses the game of being rigged
def shuffle_deck():
    print("Shuffling deck exactly 100 thousand times...")
    for i in range(10**5): random.shuffle(master_deck)
    print("Shuffling complete!")

def distribute_cards():
    for i in range(10): # Distribute 5 cards for 2 players
        if i%2 == 0: cpu_deck.append(master_deck.pop(0))
        else: player_deck.append(master_deck.pop(0))

def compare_cards():
    for i in range(5):
        player_choice = random.choice(player_deck)
        cpu_choice = random.choice(cpu_deck)

        cpu_card = cpu_choice%100
        player_card = player_choice%100

        # Compare the cards
        if cpu_card > player_card:
            cpu_win_pile.append(player_choice)
            player_deck.remove(player_choice)
            cpu_win_pile.append(cpu_choice)
            cpu_deck.remove(cpu_choice)
        elif cpu_card < player_card:
            player_win_pile.append(player_choice)
            player_deck.remove(player_choice)
            player_win_pile.append(cpu_choice)
            cpu_deck.remove(cpu_choice)
        else: i -= 1

def declare_winner():
    if len(player_win_pile) > len(cpu_win_pile): print("You win!")
    elif len(player_win_pile) < len(cpu_win_pile): print("CPU wins!")
    else: print("Tie!")

shuffle_deck()
distribute_cards()
compare_cards()
declare_winner()

# NOTE: Honestly, you could just replace all this code with this:
#
# import random
# num = random.randrange(2) # Generates either 0 or 1 randomly
# if num == 0: print("You win!")
# elif num == 1: print("CPU wins!")

