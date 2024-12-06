countries = [
{"name":"Poland", "population":38000000},
{"name":"Ukraine", "population":37000000},
{"name":"USA", "population":346224933},
{"name":"China", "population":1419321278},
{"name":"Italy", "population":59342867},
{"name":"United Kingdom", "population":69315371},
]

for country in countries:
    for key,value in country.items():
        print(f"{key} : {value}")