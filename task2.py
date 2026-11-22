import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
   
    if not all(isinstance(value, int) for value in (min, max, quantity)):
        return []

    if min < 1 or max > 1000 or min > max:
        return []

    if quantity < 1 or quantity > max - min + 1:
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)

    print(get_numbers_ticket(1, 36, 5))
    print(get_numbers_ticket(0, 49, 6))        
    print(get_numbers_ticket(1, 1001, 6)) 
    print(get_numbers_ticket(1, 10, 20)) 