def hide(card_number):
    if len(card_number) == 16:
        return card_number[0:2] + "*" * 10 + card_number[-4:]
    else:
        return "Invalid card number"