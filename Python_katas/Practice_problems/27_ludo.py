import random

# ------------------------------
# Basic configuration
# ------------------------------

TRACK_LENGTH = 28   # how many steps to finish (simple circular track)
HOME_ENTRY = 0      # index where tokens enter the track


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.position = -1  # -1 = in yard, 0..TRACK_LENGTH-1 = on track, TRACK_LENGTH = finished

    @property
    def is_finished(self):
        return self.position == TRACK_LENGTH

    def __str__(self):
        if self.position == -1:
            return f"{self.name}({self.symbol}): Yard"
        elif self.position == TRACK_LENGTH:
            return f"{self.name}({self.symbol}): Finished"
        else:
            return f"{self.name}({self.symbol}): {self.position}"


def roll_dice():
    return random.randint(1, 6)


def draw_board(players):
    """Simple linear track visualization."""
    cells = ["." for _ in range(TRACK_LENGTH)]

    for p in players:
        if 0 <= p.position < TRACK_LENGTH:
            cells[p.position] = p.symbol

    print("\nBoard:")
    print("Index: ", " ".join(f"{i:2d}" for i in range(TRACK_LENGTH)))
    print("Cells: ", " ".join(f"{c:2s}" for c in cells))
    print("Status:")
    for p in players:
        print("  ", p)
    print()


def can_move(player, dice):
    # In yard: must roll 6 to come out
    if player.position == -1:
        return dice == 6
    # On track: cannot overshoot finish
    return player.position + dice <= TRACK_LENGTH


def move_player(player, dice, players):
    # If in yard and dice == 6, enter at HOME_ENTRY
    if player.position == -1:
        if dice == 6:
            player.position = HOME_ENTRY
            print(f"{player.name} enters the board at {HOME_ENTRY}.")
        else:
            print(f"{player.name} cannot move (needs 6 to enter).")
            return
    else:
        new_pos = player.position + dice
        if new_pos > TRACK_LENGTH:
            print(f"{player.name} cannot move (would overshoot finish).")
            return
        player.position = new_pos
        if player.is_finished:
            print(f"{player.name} reached HOME!")
        else:
            print(f"{player.name} moves to {player.position}.")

    # Capture logic: if two players land on same spot, the older one goes back to yard
    if 0 <= player.position < TRACK_LENGTH:
        for other in players:
            if other is not player and other.position == player.position:
                other.position = -1
                print(f"{player.name} captures {other.name}! {other.name} goes back to yard.")


def next_player_index(current_index, players):
    n = len(players)
    i = (current_index + 1) % n
    while players[i].is_finished:
        i = (i + 1) % n
    return i


def all_others_finished(players, current_player):
    """Optional simple rule: stop when one player finishes (winner),
    or continue until all tokens finished if you want."""
    return False  # keep simple: game stops when first finishes


def setup_players():
    while True:
        try:
            n = int(input("Enter number of players (2-4): "))
            if 2 <= n <= 4:
                break
            print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    symbols = ["R", "G", "B", "Y"]
    players = []
    for i in range(n):
        name = input(f"Enter name for Player {i+1} [{symbols[i]}]: ").strip()
        if not name:
            name = f"Player{i+1}"
        players.append(Player(name, symbols[i]))
    return players


def main():
    print("=== CLI Ludo (Single Token per Player) ===")
    print("Rules (simplified):")
    print("- Each player has 1 token.")
    print("- Roll a 6 to bring the token out of the yard.")
    print("- Move along a linear track of", TRACK_LENGTH, "steps.")
    print("- Exact roll required to finish.")
    print("- Landing on another player sends them back to yard.")
    print("- First player to reach HOME wins.\n")

    players = setup_players()
    current_index = 0

    while True:
        current = players[current_index]
        if current.is_finished:
            if all_others_finished(players, current):
                break
            current_index = next_player_index(current_index, players)
            continue

        draw_board(players)

        input(f"{current.name}'s turn ({current.symbol}). Press Enter to roll dice...")
        dice = roll_dice()
        print(f"{current.name} rolled a {dice}.")

        if can_move(current, dice):
            move_player(current, dice, players)
        else:
            print(f"{current.name} cannot move this turn.")

        if current.is_finished:
            print(f"\n*** {current.name} WINS! ***")
            break

        # Extra turn on 6 (optional rule)
        if dice == 6 and not current.is_finished:
            print(f"{current.name} rolled a 6 and gets an extra turn!")
        else:
            current_index = next_player_index(current_index, players)

    print("\nFinal standings:")
    for p in players:
        print(" ", p)
    print("Game over.")


if __name__ == "__main__":
    main()
