def main():
    card_number = input("Number: ").strip()
    
    if not card_number.isdigit():
        print("INVALID")
        return

    if is_valid_luhn(card_number):
        card_type = get_card_type(card_number)
        print(card_type)
    else:
        print("INVALID")

def is_valid_luhn(number):
    total = 0
    num_digits = len(number)
    parity = num_digits % 2

    for i, digit in enumerate(number):
        digit = int(digit)
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0

def get_card_type(number):
    if len(number) == 15 and number.startswith(('34', '37')):
        return "AMEX"
    elif len(number) == 16 and number.startswith(('51', '52', '53', '54', '55')):
        return "MASTERCARD"
    elif len(number) in [13, 16] and number.startswith('4'):
        return "VISA"
    else:
        return "INVALID"

if __name__ == "__main__":
    main()
