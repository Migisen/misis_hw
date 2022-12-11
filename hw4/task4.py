from typing import List, Dict


def get_sentence_statistics(sentence: List[str]) -> Dict[str, int]:
    result = {}
    for char in sentence:
        lower_char = char.lower()
        if lower_char not in result.keys():
            result[lower_char] = 1
        else:
            sorted
            result[lower_char] += 1
    for char, count in result.items():
        print(f'{char} = {count}')
    return result


if __name__ == "__main__":
    test_sentence = 'Тут есть какие-то символы, пробел тоже считаем'
    get_sentence_statistics(test_sentence)
