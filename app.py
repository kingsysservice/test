def calculate_total(price, quantity):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    return price * quantity


def main():
    price = 10
    quantity = 3

    total = calculate_total(price, quantity)

    print(f"Price per item: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Total price: ${total}")


if __name__ == "__main__":
    main()