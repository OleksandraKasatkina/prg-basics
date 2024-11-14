from card75 import hide

card_number = input("Enter your 16-digit credit card number: ")
masked_card = hide(card_number)
print("Masked credit card number:", masked_card)