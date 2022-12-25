from typing import Optional


class ConversionError(Exception):
    def __init__(self, message):
        super().__init__(message)


def check_grade_by_points(grade, score):
    if score >= grade['min'] and score <= grade['max']:
        return True
    else:
        return False


def convert_grade_to_number(grade: str) -> Optional[str]:
    number_to_letter_mapping = {2: 'P',
                                3: [{'grade': 'E', 'min': 61, 'max': 67}, {'grade': 'D', 'min': 68, 'max': 73}],
                                4: [{'grade': 'C', 'min': 74, 'max': 83}, {'grade': 'B', 'min': 84, 'max': 90}],
                                5: 'A'}
    try:
        grade = int(grade)
    except ValueError:
        raise ConversionError(
            'Не смогли сконвертировать в буквенное, не число')

    if grade not in number_to_letter_mapping.keys():
        raise ConversionError(
            'Не смогли сконвертировать в буквенное, такой оценки нет')

    converted_grade = number_to_letter_mapping[grade]
    if isinstance(converted_grade, list):
        while True:
            try:
                score = int(input(
                    (f'Может быть 2 оценки {converted_grade}, введите кол-во баллов: ')))
                break
            except ValueError:
                print('Вы ввели не число :(')
        for possible_grade in converted_grade:
            if check_grade_by_points(possible_grade, score):
                return possible_grade['grade']
        raise ConversionError(
            'Не смогли сконвертировать в буквенное, оценки с такими баллами нет')
    else:
        return converted_grade


def convert_grade_to_letter(grade):
    letter_to_number_mapping = {'P': 2,
                                'E': 3,
                                'D': 3,
                                'C': 4,
                                'B': 4,
                                'A': 5}
    if grade not in letter_to_number_mapping.keys():
        raise ConversionError(
            'Не смогли сконвертировать в числовую, такой оценки нет :(')
    return letter_to_number_mapping[grade]


def convert_grade(grade):
    for conversion_func in [convert_grade_to_number, convert_grade_to_letter]:
        try:
            return conversion_func(grade)
        except ConversionError as ce:
            print(str(ce))


if __name__ == "__main__":
    while True:
        user_grade = input('Введите оцнеку: ')
        if user_grade == '':
            break
        print(f'Сконвертированная оценка: {convert_grade(user_grade)}')
