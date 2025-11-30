computer_games = ["Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3", "League of Legends", "Valorant", "Grand Theft Auto V", "Elden Ring", "Apex Legends", "Call of Duty: Warzone"]
computer_games.sort()
index = 0
number = 1
while index < len(computer_games):
    game_name = computer_games[index]
    print(f'{number}. {game_name}')
    index += 1
    number += 1