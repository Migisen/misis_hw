from typing import Dict


def get_ceaser_dict(shift: int) -> Dict[str, str]:
    abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ceaser_dict = {}
    last_letters = 0
    for idx in range(len(abc)):
        if idx < len(abc) - shift:
            ceaser_dict[abc[idx]] = abc[idx + shift]
        else:
            ceaser_dict[abc[idx]] = abc[last_letters]
            last_letters += 1
    return ceaser_dict


def process_ceaser(sentence: str, shift: int, action: str = 'encode', keep_case: bool = True) -> str:
    """Шифр Цезаря

    Args:
        sentence (str): исходное предложение
        shift (int): сдвиг
        action (str, optional): цель работы, доступны encode и decode. Defaults to 'encode'.
        keep_case (bool, optional): оставить ли регистр. Defaults to True.

    Returns:
        str: закодированное или декодированное предложение
    """
    if action == 'encode':
        ceaser_dict = get_ceaser_dict(shift)
    elif action == 'decode':
        ceaser_dict = get_ceaser_dict(-shift)
    else:
        raise Exception('Поддерживается только encode, decode')
    processed_sentence = ''
    for char in sentence:
        if char.lower() in ceaser_dict.keys():
            if keep_case and char.isupper():
                processed_sentence += ceaser_dict[char.lower()].upper()
            else:
                processed_sentence += ceaser_dict[char.lower()]
        else:
            processed_sentence += char

    return processed_sentence


# def decode_ceaser(sentence: str, shift: int, keep_case: bool = True):
#     # Тут получаем обратный словарь
#     ceaser_dict = get_ceaser_dict(-shift)
#     for char in sentence:
#         if char.lower() in ceaser_dict.keys():
#             if keep_case and char.isupper():
#                 encoded_sentence += ceaser_dict[char].upper()
#             else:
#                 encoded_sentence += ceaser_dict[char]
#         else:
#             encoded_sentence += char
#     return encoded_sentence


if __name__ == "__main__":
    k = 3
    print('Сохраняем регистр')
    test_sentence = 'Съешь же ещё этих мягких французских булок, да выпей чаю.'
    encoded_sentence = process_ceaser(
        test_sentence, k, action='encode', keep_case=True)
    decoded_sentence = process_ceaser(
        encoded_sentence, k, action='decode', keep_case=True)
    print(f'Закодированное предложение: \n{encoded_sentence}')
    print(f'Декодированное предложение: \n{decoded_sentence}')
    assert decoded_sentence == test_sentence

    print('---')
    print('Используем нижний регистр')
    encoded_sentence = process_ceaser(
        test_sentence, k, action='encode', keep_case=False)
    decoded_sentence = process_ceaser(
        encoded_sentence, k, action='decode', keep_case=False)
    print(f'Закодированное предложение: \n{encoded_sentence}')
    print(f'Декодированное предложение: \n{decoded_sentence}')
    assert decoded_sentence == test_sentence.lower()
