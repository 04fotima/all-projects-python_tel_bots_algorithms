

def save_data(winner_list, looser_list, counter1):
    pass

user_dict = {
    "user_1": None,
    "user_2": None,
    "user_3": None,
    "user_4": None,
}

game_count = int(input("Enter no of games: "))
counter = 0

while counter < game_count:
    for user in user_dict:
        user_dict[user] = input(f"{user} act (1 for rock, 2 for paper, 3 for scissors): ")

    rock_list = []
    paper_list = []
    scissors_list = []

    for user, choice in user_dict.items():
        if choice == "1":
            rock_list.append(user)
        elif choice == "2":
            paper_list.append(user)
        elif choice == "3":
            scissors_list.append(user)

    winner_list = []
    loser_list = []

    if len(rock_list) == 4 or len(paper_list) == 4 or len(scissors_list) == 4:
        continue

    elif len(paper_list) == 0:
        winner_list = rock_list
        loser_list = scissors_list
    elif len(rock_list) == 0:
        winner_list = scissors_list
        loser_list = paper_list
    elif len(scissors_list) == 0:
        winner_list = paper_list
        loser_list = rock_list

    counter += 1
    print("Winners:", winner_list)
    print("Losers:", loser_list)
    save_data(winner_list, loser_list, counter)