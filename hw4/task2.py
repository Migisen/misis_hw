from typing import List
import re


def find_number_in_sentences(sentences: List[str]) -> int:
    result = []
    for sentence in sentences:
        if re.search(r'\d+', sentence) is not None:
            result.append(True)
    return len(result)


if __name__ == "__main__":
    test_sentences = ['Привет 123, мир!',
                      'Цифр4 вну7ри', 'Тут нет', 'Тут 2 есть']

    print(find_number_in_sentences(test_sentences))
