def binary_search() -> int:
    numbers = list(range(1, 101))
    steps = 0
    while len(numbers) != 1:
        steps += 1
        predicted_number = numbers[len(numbers)//2]
        user_answer = int(input(
            f'Твое число равно, меньше или больше, чем число {predicted_number}?'))
        match user_answer:
            case 1:
                print(
                    f'Твое число равно = {predicted_number}, угадали за {steps} шагов')
                return predicted_number
            case 2:
                numbers = numbers[len(numbers)//2+1:]
            case 3:
                numbers = numbers[:len(numbers)//2]
        print(numbers)
    print(f'Твое число равно = {numbers[0]}, угадали за {steps} шагов')
    return numbers[0]


if __name__ == "__main__":
    binary_search()
