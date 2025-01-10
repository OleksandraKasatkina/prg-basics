temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

positive_temp_cities = list(filter(lambda city: temp[city] > 0, temp.keys()))

print('Cities with positive temperatures:', *positive_temp_cities)