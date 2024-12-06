person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":
   {"landline":"123444321",
    "mobile":"777888999"}
}

print(person["name"])
print(person["hobby"])

for key,value in person.items():
   print(f"{key} : {value}")

person["surname"] = "Nowak"
person["married"] = False

person["gender"] = "male"
person["hobby"].append("bicycle")

person['phone']['work phone'] = '313131444'

for key,value in person.items():
   print(f"{key} : {value}")