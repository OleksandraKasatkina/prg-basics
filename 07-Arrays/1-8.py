computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games.sort()

index = 1
while index <= len(computer_games):
    print(f'{index}) {computer_games[index - 1]}')
    index += 1