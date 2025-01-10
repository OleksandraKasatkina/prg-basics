medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

countries_with_10_medals = list(filter(lambda country: country["gold"] + country["silver"] + country["bronze"] >= 10, medal_data))

print("COUNTRIES WITH AT LEAST 10 MEDALS")
for country in countries_with_10_medals:
    print(f'{country["country"]}: {country["gold"]},{country["silver"]},{country["bronze"]}')