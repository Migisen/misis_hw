if __name__ == "__main__":
    strings = ['a', 'b', 'c', 'd', 'e']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    results = [(strings[idx], numbers[idx])
               for idx in range(min(len(strings), len(numbers)))]

    print(results)
